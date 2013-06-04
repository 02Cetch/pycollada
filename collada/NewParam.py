from .common import DaeObject, tag
from .SIDREF import SIDREF

class NewParam(DaeObject):
    def __init__(self, sid, value, xmlnode):
        self.sid = sid
        self.value = value
        self.xmlnode = xmlnode

    @staticmethod
    def load( collada, localscope, scoped_node_for_sids, node ):
        sid = node.get('sid')
        value = None
        for child in node.getchildren():
            if child.tag == tag('float') or child.tag == tag('int') or child.tag == tag('bool'):
                value = child.text
                break
            elif child.tag == tag('SIDREF'):
                value = SIDREF.load(collada, localscope, scoped_node_for_sids, child)
                break
        newparam = NewParam(sid, value, node)
        collada.addSid(sid, newparam)
        return newparam

    @staticmethod
    def loadnewparams(collada, xmlnode):
        """returns all newparams from children of node"""
        newparam_nodes = xmlnode.findall(tag('newparam')) or []
        print 'newparam_nodes is', newparam_nodes
        return [NewParam.load(collada, {}, None, newparam_node) for newparam_node in newparam_nodes]

    # FIXME: should this return [] if self.value is not a DaeObject (e.g. a float)?
    #        or, should we make DaeObjects for floats and such?
    def getchildren(self):
        if isinstance(self.value, SIDREF):
            return [ self.value ]
        else:
            return []

    # FIXME: does not handle cycles!
    def resolve(self):
        newparam = self
        while type(newparam) == SIDREF or type(newparam) == NewParam:
            if type(newparam) == SIDREF:
                newparam = newparam.resolve()
            else:
                newparam = newparam.value
        return newparam

