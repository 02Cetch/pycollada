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
"""Contains objects for representing a kinematics link."""

from .common import DaeObject, E, tag, get_number_dtype, float_format_func
from .common import DaeIncompleteError, DaeBrokenRefError, DaeMalformedError, DaeUnsupportedError
from .xmlutil import etree as ElementTree
from .util import toUnitVec
import numpy

def makeRotationMatrix(x, y, z, angle):
    """Build and return a transform 4x4 matrix to rotate `angle` radians
    around (`x`,`y`,`z`) axis."""
    c = numpy.cos(angle)
    s = numpy.sin(angle)
    t = (1-c)
    return numpy.array([[t*x*x+c,     t*x*y - s*z, t*x*z + s*y, 0],
                        [t*x*y+s*z,   t*y*y + c,   t*y*z - s*x, 0],
                        [t*x*z - s*y, t*y*z + s*x, t*z*z + c,   0],
                        [0,           0,           0,           1]],
                       dtype=get_number_dtype() )


class Transform(DaeObject):
    """Base class for all transformation types"""

    def getchildren(self):
        return []

    def save(self):
        pass


class TranslateTransform(Transform):
    """Contains a translation transformation as defined in the collada <translate> tag."""

    def __init__(self, x, y, z, sid=None, xmlnode=None):
        """Creates a translation transformation

        :param float x:
          x coordinate
        :param float y:
          y coordinate
        :param float z:
          z coordinate
        :param xmlnode:
           When loaded, the xmlnode it comes from

        """
        self.x = x
        """x coordinate"""
        self.y = y
        """y coordinate"""
        self.z = z
        """z coordinate"""
        self.matrix = numpy.identity(4, dtype=get_number_dtype())
        """The resulting transformation matrix. This will be a numpy.array of size 4x4."""
        self.matrix[:3,3] = [ x, y, z ]
        self.sid = sid
        self.xmlnode = xmlnode
        """ElementTree representation of the transform."""
        if xmlnode is None:
            self.xmlnode = E.translate()
            self.save(0)
            
    @staticmethod
    def load(collada, node):
        sid=node.get('sid')
        floats = numpy.fromstring(node.text, dtype=get_number_dtype(), sep=' ')
        if len(floats) != 3:
            raise DaeMalformedError("Translate node requires three float values")
        ttransform = TranslateTransform(floats[0], floats[1], floats[2], sid, node)
        collada.addSid(sid, ttransform)
        return ttransform

    def save(self,recurse=True):
        """Saves the info back to :attr:`xmlnode`"""
        if self.sid is not None:
            self.xmlnode.set('sid',self.sid)
        else:
            self.xmlnode.attrib.pop('sid',None)
        self.xmlnode.text = ' '.join(map(float_format_func(), [self.x, self.y, self.z]))

    def __str__(self):
        return '<TranslateTransform (%.15e, %.15e, %.15e)>' % (self.x, self.y, self.z)

    def __repr__(self):
        return str(self)
        
class RotateTransform(Transform):
    """Contains a rotation transformation as defined in the collada <rotate> tag."""

    def __init__(self, x, y, z, angle, sid=None, xmlnode=None):
        """Creates a rotation transformation

        :param float x:
          x coordinate
        :param float y:
          y coordinate
        :param float z:
          z coordinate
        :param float angle:
          angle of rotation, in radians
        :param xmlnode:
           When loaded, the xmlnode it comes from

        """
        self.x = x
        """x coordinate"""
        self.y = y
        """y coordinate"""
        self.z = z
        """z coordinate"""
        self.angle = angle
        """angle of rotation, in radians"""
        self.matrix = makeRotationMatrix(x, y, z, angle*numpy.pi/180.0)
        self.sid = sid
        """The resulting transformation matrix. This will be a numpy.array of size 4x4."""
        self.xmlnode = xmlnode
        """ElementTree representation of the transform."""
        if xmlnode is None:
            self.xmlnode = E.rotate()
            self.save(0)

    @staticmethod
    def load(collada, node):
        sid=node.get('sid')
        floats = numpy.fromstring(node.text, dtype=get_number_dtype(), sep=' ')
        if len(floats) != 4:
            raise DaeMalformedError("Rotate node requires four float values")
        rtransform = RotateTransform(floats[0], floats[1], floats[2], floats[3], sid, node)
        collada.addSid(sid, rtransform)
        return rtransform

    def save(self,recurse=True):
        """Saves the info back to :attr:`xmlnode`"""
        if self.sid is not None:
            self.xmlnode.set('sid',self.sid)
        else:
            self.xmlnode.attrib.pop('sid',None)
        self.xmlnode.text = ' '.join(map(float_format_func(), [self.x, self.y, self.z, self.angle]))

    def __str__(self):
        return '<RotateTransform (%.15e, %.15e, %.15e) angle=%.15e>' % (self.x, self.y, self.z, self.angle)

    def __repr__(self):
        return str(self)


class ScaleTransform(Transform):
    """Contains a scale transformation as defined in the collada <scale> tag."""

    def __init__(self, x, y, z, sid=None, xmlnode=None):
        """Creates a scale transformation

        :param float x:
          x coordinate
        :param float y:
          y coordinate
        :param float z:
          z coordinate
        :param xmlnode:
           When loaded, the xmlnode it comes from

        """
        self.x = x
        """x coordinate"""
        self.y = y
        """y coordinate"""
        self.z = z
        """z coordinate"""
        self.matrix = numpy.identity(4, dtype=get_number_dtype())
        """The resulting transformation matrix. This will be a numpy.array of size 4x4."""
        self.matrix[0,0] = x
        self.matrix[1,1] = y
        self.matrix[2,2] = z
        self.sid = sid
        self.xmlnode = xmlnode
        """ElementTree representation of the transform."""
        if xmlnode is None:
            self.xmlnode = E.scale(' '.join(map(float_format_func(), [x, y, z])))
            
    @staticmethod
    def load(collada, node):
        sid=node.get('sid')
        floats = numpy.fromstring(node.text, dtype=get_number_dtype(), sep=' ')
        if len(floats) != 3:
            raise DaeMalformedError("Scale node requires three float values")
        stransform = ScaleTransform(floats[0], floats[1], floats[2], sid, node)
        collada.addSid(sid, stransform)
        return stransform

    def save(self,recurse=True):
        """Saves the info back to :attr:`xmlnode`"""
        if self.sid is not None:
            self.xmlnode.set('sid',self.sid)
        else:
            self.xmlnode.attrib.pop('sid',None)
        self.xmlnode.text = ' '.join(map(float_format_func(), [self.x, self.y, self.z]))

    def __str__(self):
        return '<ScaleTransform (%.15e, %.15e, %.15e)>' % (self.x, self.y, self.z)

    def __repr__(self):
        return str(self)


class MatrixTransform(Transform):
    """Contains a matrix transformation as defined in the collada <matrix> tag."""

    def __init__(self, matrix, sid=None, xmlnode=None):
        """Creates a matrix transformation

        :param numpy.array matrix:
          This should be an unshaped numpy array of floats of length 16
        :param xmlnode:
           When loaded, the xmlnode it comes from

        """
        self.matrix = matrix
        """The resulting transformation matrix. This will be a numpy.array of size 4x4."""
        if len(self.matrix) != 16: raise DaeMalformedError('Corrupted matrix transformation node')
        self.matrix.shape = (4, 4)
        self.sid = sid
        self.xmlnode = xmlnode
        """ElementTree representation of the transform."""
        if xmlnode is None:
            self.xmlnode = E.matrix()
            self.save(0)

    @staticmethod
    def load(collada, node):
        sid=node.get('sid')
        floats = numpy.fromstring(node.text, dtype=get_number_dtype(), sep=' ')
        mtransform = MatrixTransform(floats, sid, node)
        collada.addSid(sid, mtransform)
        return mtransform

    def save(self,recurse=True):
        """Saves the info back to :attr:`xmlnode`"""
        if self.sid is not None:
            self.xmlnode.set('sid',self.sid)
        else:
            self.xmlnode.attrib.pop('sid',None)
        self.xmlnode.text = ' '.join(map(float_format_func(), self.matrix.flat))

    def __str__(self):
        return '<MatrixTransform>'

    def __repr__(self):
        return str(self)


class LookAtTransform(Transform):
    """Contains a transformation for aiming a camera as defined in the collada <lookat> tag."""

    def __init__(self, eye, interest, upvector, sid=None, xmlnode=None):
        """Creates a lookat transformation

        :param numpy.array eye:
          An unshaped numpy array of floats of length 3 containing the position of the eye
        :param numpy.array interest:
          An unshaped numpy array of floats of length 3 containing the point of interest
        :param numpy.array upvector:
          An unshaped numpy array of floats of length 3 containing the up-axis direction
        :param xmlnode:
          When loaded, the xmlnode it comes from

        """
        self.eye = eye
        """A numpy array of length 3 containing the position of the eye"""
        self.interest = interest
        """A numpy array of length 3 containing the point of interest"""
        self.upvector = upvector
        """A numpy array of length 3 containing the up-axis direction"""

        if len(eye) != 3 or len(interest) != 3 or len(upvector) != 3:
            raise DaeMalformedError('Corrupted lookat transformation node')

        self.matrix = numpy.identity(4, dtype=get_number_dtype())
        """The resulting transformation matrix. This will be a numpy.array of size 4x4."""

        front = toUnitVec(numpy.subtract(eye,interest))
        side = numpy.multiply(-1, toUnitVec(numpy.cross(front, upvector)))
        self.matrix[0,0:3] = side
        self.matrix[1,0:3] = upvector
        self.matrix[2,0:3] = front
        self.matrix[3,0:3] = eye
        self.sid = sid
        self.xmlnode = xmlnode
        """ElementTree representation of the transform."""
        if xmlnode is None:
            self.xmlnode = E.lookat()
            self.save(0)

    @staticmethod
    def load(collada, node):
        sid=node.get('sid')
        floats = numpy.fromstring(node.text, dtype=get_number_dtype(), sep=' ')
        if len(floats) != 9:
            raise DaeMalformedError("Lookat node requires 9 float values")
        latransform = LookAtTransform(floats[0:3], floats[3:6], floats[6:9], sid, node)
        collada.addSid(sid, latransform)
        return latransform
    
    def save(self,recurse=True):
        """Saves the info back to :attr:`xmlnode`"""
        if self.sid is not None:
            self.xmlnode.set('sid',self.sid)
        else:
            self.xmlnode.attrib.pop('sid',None)
        self.xmlnode.text = ' '.join(map(float_format_func(), numpy.concatenate((self.eye, self.interest, self.upvector)) ))
        
    def __str__(self):
        return '<LookAtTransform>'

    def __repr__(self):
        return str(self)
