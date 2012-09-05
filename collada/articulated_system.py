####################################################################
#                                                                  #
# THIS FILE IS PART OF THE pycollada LIBRARY SOURCE CODE.          #
# USE, DISTRIBUTION AND REPRODUCTION OF THIS LIBRARY SOURCE IS     #
# GOVERNED BY A BSD-STYLE SOURCE LICENSE INCLUDED WITH THIS SOURCE #
# IN 'COPYING'. PLEASE READ THESE TERMS BEFORE DISTRIBUTING.       #
#                                                                  #
# THE pycollada SOURCE CODE IS (C) COPYRIGHT 2011                  #
# by Jeff Terrace and contributors                                 #
#                                                                  #
####################################################################

"""Contains objects for representing an articulated system."""

import numpy

from .common import DaeObject, E, tag
from .common import DaeIncompleteError, DaeBrokenRefError, DaeMalformedError, DaeUnsupportedError
from .xmlutil import etree as ElementTree
from .kinematics_model import InstanceKinematicsModel

class InstanceArticulatedSystem(object):
    def __init__(self,url, sid='', name='', xmlnode=None):
        self.url = url
        self.sid = sid
        self.name = name
        if xmlnode is not None:
            self.xmlnode = xmlnode
        else:
            self.xmlnode = E.instance_articulated_system()
            self.save()

    def save(self):
        """Saves the info back to :attr:`xmlnode`"""
        self.xmlnode.set('url',url)
        if self.sid is not None:
            self.xmlnode.set('sid',self.sid)
        else:
            self.xmlnode.attrib.pop('sid',None)
        if self.name is not None:
            self.xmlnode.set('name',self.name)
        else:
            self.xmlnode.attrib.pop('name',None)
            
class Kinematics(object):
    """A class containing the data coming from a COLLADA <kinematics> tag"""
    def __init__(self, collada, kinematics_models=None, instance_kinematics_models=None,axisinfos=None,xmlnode=None):
        """Create a <kinematics>

        :param list kinematics_models: a resolved KinematicsModel
        :param list instance_kinematics_models: a InstanceKinematicsModel if could not resolve
        :param list axisinfos: list of xmlnodes
        :param xmlnode:
        When loaded, the xmlnode it comes from
        """
        self.kinematics_models = []
        if kinematics_models is not None:
            self.kinematics_models = kinematics_models
        self.instance_kinematics_models = []
        if instance_kinematics_models is not None:
            self.instance_kinematics_models = instance_kinematics_models
        self.axisinfos = axisinfos
        if xmlnode != None:
            self.xmlnode = xmlnode
        else:
            self.xmlnode = E.kinematics(*self.axisinfos)
            self.xmlnode.append(E.technique_common())
        self.xmlnode = xmlnode
        
    @staticmethod
    def load(collada, node):
        kinematics_models = []
        instance_kinematics_models = []
        axisinfos = []
        for subnode in node:
            if subnode.tag == tag('instance_kinematics_model'):
                url=subnode.get('url')
                if url is not None:
                    if url.startswith('#'): # inside this doc, so search for it
                        kmodel = collada.kinematics_models.get(url[1:])
                        if kmodel is None:
                            raise DaeBrokenRefError('kinematics_model %s not found in library'%url)

                        kinematics_models.append(kmodel)
                    else:
                        instance_kinematics_models.append(InstanceKinematicsModel(url,xmlnode=subnode)) # external reference
            elif subnode.tag == tag('technique_common'):
                for subsubnode in subnode:
                    if subsubnode == tag('axis_info'):
                        axisinfos.append(subsubnode)
                        # parse <limits>?
        return Kinematics(collada, kinematics_models, instance_kinematics_models,axisinfos,xmlnode=node)

    def save(self):
        """Saves the kinematics node back to :attr:`xmlnode`"""
        #self.xmlnode.
        for kmodel in self.kinematics_models:
            ikmodel = E.instance_kinematics_model()
            ikmodel.set('url','#'+kmodel.id)
            self.xmlnode.append(ikmodel)
        
        #self.xmlnode.set('url', "#%s" % self.geometry.id)
        #self.instance_kinematics_models
        #self.axisinfos
        #instance_kinematics_models
        

class Motion(object):
    """A class containing the data coming from a COLLADA <motion> tag"""
    def __init__(self, collada, articulated_system=None,instance_articulated_system=None,axisinfos=None,xmlnode=None):
        """Create a <motion>

        :param articulated_system: a resolved ArticultedSystem
        :param instance_articulated_system: a InstanceArticulatedSystem if could not resolve
        :param list axisinfos: list of xmlnodes
        :param xmlnode:
        When loaded, the xmlnode it comes from
        """
        self.articulated_system = articulated_system
        self.instance_articulated_system = instance_articulated_system
        self.axisinfos = axisinfos
        if xmlnode != None:
            self.xmlnode = xmlnode
        else:
            self.xmlnode = E.motion(*self.axisinfos)
            self.xmlnode.append(E.technique_common())
            if self.articulated_system is not None:
                pass
            elif self.instance_articulated_system is not None:
                self.xmlnode.append(self.instance_articulated_system.xmlnode)
        
    @staticmethod
    def load(collada, node):
        instance_articulated_system = None
        articulated_system = None
        axisinfos = []
        for subnode in node:
            if subnode.tag == tag('instance_articulated_system'):
                url=subnode.get('url')
                if url is not None:
                    if url.startswith('#'):
                        articulated_system = collada.articulated_systems.get(url[1:])
                        if articulated_system is None:
                            raise DaeBrokenRefError('articulated_system %s not found in library'%url)
                        
                    else:
                        instance_articulated_system = InstanceArticulatedSystem(url,subnode.get('sid'), subnode.get('name'), xmlnode=subnode) # external reference
            elif subnode.tag == tag('technique_common'):
                for subsubnode in subnode:
                    if subsubnode == tag('axis_info'):
                        axisinfos.append(subsubnode)
                        # parse <speed>, <acceleration>, <deceleration>, <jerk>?
        return Motion(collada, articulated_system,instance_articulated_system,axisinfos,xmlnode=node)

class ArticulatedSystem(DaeObject):
    """A class containing the data coming from a COLLADA <articulated_system> tag"""
    def __init__(self, collada, id, name, kinematics=None, motion=None, xmlnode=None):
        """Create a articulated_system instance

          :param collada.Collada collada:
            The collada object this geometry belongs to
          :param str id:
            A unique string identifier for the geometry
          :param str name:
            A text string naming the geometry
          :param kinematics: Kinematics object
          :param motion: Motion object
          :param xmlnode:
            When loaded, the xmlnode it comes from.

        """
        self.collada = collada
        """The :class:`collada.Collada` object this geometry belongs to"""

        self.id = id
        """The unique string identifier for the geometry"""

        self.name = name
        """The text string naming the geometry"""

        self.kinematics = kinematics

        if xmlnode != None:
            self.xmlnode = xmlnode
            """ElementTree representation of the geometry."""
        else:
            if self.kinematics is not None:
                self.xmlnode = E.articulated_system(self.kinematics.xmlnode)
            else:
                self.xmlnode = E.articulated_system(self.motion.xmlnode)
            if len(self.id) > 0: self.xmlnode.set("id", self.id)
            if len(self.name) > 0: self.xmlnode.set("name", self.name)

    @staticmethod
    def load( collada, localscope, node ):
        id = node.get("id") or ""
        name = node.get("name") or ""
        motion = None
        kinematics = None
        kinematicsnode = node.find(tag('kinematics'))
        if kinematicsnode is None:
            motionnode = node.find(tag('motion'))
            if motionnode is None:
                raise DaeUnsupportedError('artiuclated_system needs to have kinematics or motion node')

            motion = Motion.load(collada, motionnode)
        else:
            kinematics = Kinematics.load(collada, kinematicsnode)
        node = ArticulatedSystem(collada, id, name, kinematics, motion, xmlnode=node )
        return node

    def save(self):
        """Saves the info back to :attr:`xmlnode`"""
        if self.kinematics is not None:
            self.kinematics.save()
            node = self.xmlnode.find(tag('kinematics'))
            if node is not None:
                node.remove()
            self.xmlnode.append(self.kinematics)
        if self.motion is not None:
            self.motion.save()
            node = self.xmlnode.find(tag('motion'))
            if node is not None:
                node.remove()
            self.xmlnode.append(self.motion)
        self.xmlnode.set('id', self.id)
        self.xmlnode.set('name', self.name)
