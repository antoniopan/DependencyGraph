# .\build_config.py
# -*- coding: utf-8 -*-
# PyXB bindings for NM:e92452c8d3e28a9e27abfc9994d2007779e7f4c9
# Generated 2022-06-11 21:57:27.537020 by PyXB version 1.2.6 using Python 3.7.8.final.0
# Namespace AbsentNamespace0

from __future__ import unicode_literals
import pyxb
import pyxb.binding
import pyxb.binding.saxer
import io
import pyxb.utils.utility
import pyxb.utils.domutils
import sys
import pyxb.utils.six as _six
# Unique identifier for bindings created at the same time
_GenerationUID = pyxb.utils.utility.UniqueIdentifier('urn:uuid:6d995b6e-e98e-11ec-bb56-ec5c682b06ac')

# Version of PyXB used to generate the bindings
_PyXBVersion = '1.2.6'
# Generated bindings are not compatible across PyXB versions
if pyxb.__version__ != _PyXBVersion:
    raise pyxb.PyXBVersionError(_PyXBVersion)

# A holder for module-level binding classes so we can access them from
# inside class definitions where property names may conflict.
_module_typeBindings = pyxb.utils.utility.Object()

# Import bindings for namespaces imported into schema
import pyxb.binding.datatypes

# NOTE: All namespace declarations are reserved within the binding
Namespace = pyxb.namespace.CreateAbsentNamespace()
Namespace.configureCategories(['typeBinding', 'elementBinding'])

def CreateFromDocument (xml_text, default_namespace=None, location_base=None):
    """Parse the given XML and use the document element to create a
    Python instance.

    @param xml_text An XML document.  This should be data (Python 2
    str or Python 3 bytes), or a text (Python 2 unicode or Python 3
    str) in the L{pyxb._InputEncoding} encoding.

    @keyword default_namespace The L{pyxb.Namespace} instance to use as the
    default namespace where there is no default namespace in scope.
    If unspecified or C{None}, the namespace of the module containing
    this function will be used.

    @keyword location_base: An object to be recorded as the base of all
    L{pyxb.utils.utility.Location} instances associated with events and
    objects handled by the parser.  You might pass the URI from which
    the document was obtained.
    """

    if pyxb.XMLStyle_saxer != pyxb._XMLStyle:
        dom = pyxb.utils.domutils.StringToDOM(xml_text)
        return CreateFromDOM(dom.documentElement, default_namespace=default_namespace)
    if default_namespace is None:
        default_namespace = Namespace.fallbackNamespace()
    saxer = pyxb.binding.saxer.make_parser(fallback_namespace=default_namespace, location_base=location_base)
    handler = saxer.getContentHandler()
    xmld = xml_text
    if isinstance(xmld, _six.text_type):
        xmld = xmld.encode(pyxb._InputEncoding)
    saxer.parse(io.BytesIO(xmld))
    instance = handler.rootObject()
    return instance

def CreateFromDOM (node, default_namespace=None):
    """Create a Python instance from the given DOM node.
    The node tag must correspond to an element declaration in this module.

    @deprecated: Forcing use of DOM interface is unnecessary; use L{CreateFromDocument}."""
    if default_namespace is None:
        default_namespace = Namespace.fallbackNamespace()
    return pyxb.binding.basis.element.AnyCreateFromDOM(node, default_namespace)


# Complex type parallel_buildType with content type ELEMENT_ONLY
class parallel_buildType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type parallel_buildType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'parallel_buildType')
    _XSDLocation = pyxb.utils.utility.Location('E:\\Code\\Python\\DependencyGraph\\build_config.xsd', 5, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element text_path uses Python identifier text_path
    __text_path = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'text_path'), 'text_path', '__AbsentNamespace0_parallel_buildType_text_path', False, pyxb.utils.utility.Location('E:\\Code\\Python\\DependencyGraph\\build_config.xsd', 7, 3), )

    
    text_path = property(__text_path.value, __text_path.set, None, None)

    
    # Element dox_path uses Python identifier dox_path
    __dox_path = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'dox_path'), 'dox_path', '__AbsentNamespace0_parallel_buildType_dox_path', False, pyxb.utils.utility.Location('E:\\Code\\Python\\DependencyGraph\\build_config.xsd', 8, 3), )

    
    dox_path = property(__dox_path.value, __dox_path.set, None, None)

    
    # Element num_thread uses Python identifier num_thread
    __num_thread = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'num_thread'), 'num_thread', '__AbsentNamespace0_parallel_buildType_num_thread', False, pyxb.utils.utility.Location('E:\\Code\\Python\\DependencyGraph\\build_config.xsd', 9, 3), )

    
    num_thread = property(__num_thread.value, __num_thread.set, None, None)

    
    # Element dependency_parser uses Python identifier dependency_parser
    __dependency_parser = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'dependency_parser'), 'dependency_parser', '__AbsentNamespace0_parallel_buildType_dependency_parser', False, pyxb.utils.utility.Location('E:\\Code\\Python\\DependencyGraph\\build_config.xsd', 10, 3), )

    
    dependency_parser = property(__dependency_parser.value, __dependency_parser.set, None, None)

    
    # Element graph_parser uses Python identifier graph_parser
    __graph_parser = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'graph_parser'), 'graph_parser', '__AbsentNamespace0_parallel_buildType_graph_parser', False, pyxb.utils.utility.Location('E:\\Code\\Python\\DependencyGraph\\build_config.xsd', 11, 3), )

    
    graph_parser = property(__graph_parser.value, __graph_parser.set, None, None)

    
    # Element repo_builder uses Python identifier repo_builder
    __repo_builder = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'repo_builder'), 'repo_builder', '__AbsentNamespace0_parallel_buildType_repo_builder', False, pyxb.utils.utility.Location('E:\\Code\\Python\\DependencyGraph\\build_config.xsd', 12, 3), )

    
    repo_builder = property(__repo_builder.value, __repo_builder.set, None, None)

    _ElementMap.update({
        __text_path.name() : __text_path,
        __dox_path.name() : __dox_path,
        __num_thread.name() : __num_thread,
        __dependency_parser.name() : __dependency_parser,
        __graph_parser.name() : __graph_parser,
        __repo_builder.name() : __repo_builder
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.parallel_buildType = parallel_buildType
Namespace.addCategoryObject('typeBinding', 'parallel_buildType', parallel_buildType)


parallel_build = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'parallel_build'), parallel_buildType, location=pyxb.utils.utility.Location('E:\\Code\\Python\\DependencyGraph\\build_config.xsd', 4, 1))
Namespace.addCategoryObject('elementBinding', parallel_build.name().localName(), parallel_build)



parallel_buildType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'text_path'), pyxb.binding.datatypes.string, scope=parallel_buildType, location=pyxb.utils.utility.Location('E:\\Code\\Python\\DependencyGraph\\build_config.xsd', 7, 3)))

parallel_buildType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'dox_path'), pyxb.binding.datatypes.string, scope=parallel_buildType, location=pyxb.utils.utility.Location('E:\\Code\\Python\\DependencyGraph\\build_config.xsd', 8, 3)))

parallel_buildType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'num_thread'), pyxb.binding.datatypes.int, scope=parallel_buildType, location=pyxb.utils.utility.Location('E:\\Code\\Python\\DependencyGraph\\build_config.xsd', 9, 3)))

parallel_buildType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'dependency_parser'), pyxb.binding.datatypes.string, scope=parallel_buildType, location=pyxb.utils.utility.Location('E:\\Code\\Python\\DependencyGraph\\build_config.xsd', 10, 3)))

parallel_buildType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'graph_parser'), pyxb.binding.datatypes.string, scope=parallel_buildType, location=pyxb.utils.utility.Location('E:\\Code\\Python\\DependencyGraph\\build_config.xsd', 11, 3)))

parallel_buildType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'repo_builder'), pyxb.binding.datatypes.string, scope=parallel_buildType, location=pyxb.utils.utility.Location('E:\\Code\\Python\\DependencyGraph\\build_config.xsd', 12, 3)))

def _BuildAutomaton ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton
    del _BuildAutomaton
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(parallel_buildType._UseForTag(pyxb.namespace.ExpandedName(None, 'text_path')), pyxb.utils.utility.Location('E:\\Code\\Python\\DependencyGraph\\build_config.xsd', 7, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(parallel_buildType._UseForTag(pyxb.namespace.ExpandedName(None, 'dox_path')), pyxb.utils.utility.Location('E:\\Code\\Python\\DependencyGraph\\build_config.xsd', 8, 3))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(parallel_buildType._UseForTag(pyxb.namespace.ExpandedName(None, 'num_thread')), pyxb.utils.utility.Location('E:\\Code\\Python\\DependencyGraph\\build_config.xsd', 9, 3))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(parallel_buildType._UseForTag(pyxb.namespace.ExpandedName(None, 'dependency_parser')), pyxb.utils.utility.Location('E:\\Code\\Python\\DependencyGraph\\build_config.xsd', 10, 3))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(parallel_buildType._UseForTag(pyxb.namespace.ExpandedName(None, 'graph_parser')), pyxb.utils.utility.Location('E:\\Code\\Python\\DependencyGraph\\build_config.xsd', 11, 3))
    st_4 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(parallel_buildType._UseForTag(pyxb.namespace.ExpandedName(None, 'repo_builder')), pyxb.utils.utility.Location('E:\\Code\\Python\\DependencyGraph\\build_config.xsd', 12, 3))
    st_5 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
         ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
         ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
         ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
         ]))
    st_4._set_transitionSet(transitions)
    transitions = []
    st_5._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
parallel_buildType._Automaton = _BuildAutomaton()

