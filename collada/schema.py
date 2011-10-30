#encoding:UTF-8
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

"""This module contains helper classes and functions for working
with the COLLADA 1.4.1 schema."""

import lxml
from collada.util import bytes, BytesIO

COLLADA_SCHEMA_1_4_1 = """<?xml version="1.0" encoding="utf-8"?>
<xs:schema xmlns="http://www.collada.org/2005/11/COLLADASchema" xmlns:xs="http://www.w3.org/2001/XMLSchema" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" targetNamespace="http://www.collada.org/2005/11/COLLADASchema" elementFormDefault="qualified" version="1.4.1" xml:lang="EN" xsi:schemaLocation="http://www.w3.org/2001/XMLSchema http://www.w3.org/2001/XMLSchema.xsd">
    <!-- BEGIN COLLADA Format Schema -->
    <xs:annotation>
        <xs:documentation>
              COLLADA Schema
              Version 1.4.1 (June 23, 2006)

              Copyright (C) 2005, 2006 The Khronos Group Inc., Sony Computer Entertainment Inc.
             All Rights Reserved.

             Khronos is a trademark of The Khronos Group Inc.
             COLLADA is a trademark of Sony Computer Entertainment Inc. used by permission by Khronos.

             Note that this software document is distributed on an "AS IS" basis, with ALL EXPRESS AND
             IMPLIED WARRANTIES AND CONDITIONS DISCLAIMED, INCLUDING, WITHOUT LIMITATION, ANY IMPLIED
             WARRANTIES AND CONDITIONS OF MERCHANTABILITY, SATISFACTORY QUALITY, FITNESS FOR A PARTICULAR
             PURPOSE, AND NON-INFRINGEMENT.
        </xs:documentation>
    </xs:annotation>
    <!-- import needed for xml:base attribute-->
    <xs:import namespace="http://www.w3.org/XML/1998/namespace" schemaLocation="http://www.w3.org/2001/03/xml.xsd"/>
    <!-- Root Element -->
    <xs:element name="COLLADA">
        <xs:annotation>
            <xs:appinfo>enable-xmlns</xs:appinfo>
            <xs:documentation>
            The COLLADA element declares the root of the document that comprises some of the content
            in the COLLADA schema.
            </xs:documentation>
        </xs:annotation>
        <xs:complexType>
            <xs:sequence>
                <xs:element ref="asset">
                    <xs:annotation>
                        <xs:documentation>
                        The COLLADA element must contain an asset element.
                        </xs:documentation>
                    </xs:annotation>
                </xs:element>
                <xs:choice minOccurs="0" maxOccurs="unbounded">
                    <xs:element ref="library_animations">
                        <xs:annotation>
                            <xs:documentation>
                            The COLLADA element may contain any number of library_animations elements.
                            </xs:documentation>
                        </xs:annotation>
                    </xs:element>
                    <xs:element ref="library_animation_clips">
                        <xs:annotation>
                            <xs:documentation>
                            The COLLADA element may contain any number of library_animation_clips elements.
                            </xs:documentation>
                        </xs:annotation>
                    </xs:element>
                    <xs:element ref="library_cameras">
                        <xs:annotation>
                            <xs:documentation>
                            The COLLADA element may contain any number of library_cameras elements.
                            </xs:documentation>
                        </xs:annotation>
                    </xs:element>
                    <xs:element ref="library_controllers">
                        <xs:annotation>
                            <xs:documentation>
                            The COLLADA element may contain any number of library_controllerss elements.
                            </xs:documentation>
                        </xs:annotation>
                    </xs:element>
                    <xs:element ref="library_geometries">
                        <xs:annotation>
                            <xs:documentation>
                            The COLLADA element may contain any number of library_geometriess elements.
                            </xs:documentation>
                        </xs:annotation>
                    </xs:element>
                    <xs:element ref="library_effects">
                        <xs:annotation>
                            <xs:documentation>
                            The COLLADA element may contain any number of library_effects elements.
                            </xs:documentation>
                        </xs:annotation>
                    </xs:element>
                    <xs:element ref="library_force_fields">
                        <xs:annotation>
                            <xs:documentation>
                            The COLLADA element may contain any number of library_force_fields elements.
                            </xs:documentation>
                        </xs:annotation>
                    </xs:element>
                    <xs:element ref="library_images">
                        <xs:annotation>
                            <xs:documentation>
                            The COLLADA element may contain any number of library_images elements.
                            </xs:documentation>
                        </xs:annotation>
                    </xs:element>
                    <xs:element ref="library_lights">
                        <xs:annotation>
                            <xs:documentation>
                            The COLLADA element may contain any number of library_lights elements.
                            </xs:documentation>
                        </xs:annotation>
                    </xs:element>
                    <xs:element ref="library_materials">
                        <xs:annotation>
                            <xs:documentation>
                            The COLLADA element may contain any number of library_materials elements.
                            </xs:documentation>
                        </xs:annotation>
                    </xs:element>
                    <xs:element ref="library_nodes">
                        <xs:annotation>
                            <xs:documentation>
                            The COLLADA element may contain any number of library_nodes elements.
                            </xs:documentation>
                        </xs:annotation>
                    </xs:element>
                    <xs:element ref="library_physics_materials">
                        <xs:annotation>
                            <xs:documentation>
                            The COLLADA element may contain any number of library_materials elements.
                            </xs:documentation>
                        </xs:annotation>
                    </xs:element>
                    <xs:element ref="library_physics_models">
                        <xs:annotation>
                            <xs:documentation>
                            The COLLADA element may contain any number of library_physics_models elements.
                            </xs:documentation>
                        </xs:annotation>
                    </xs:element>
                    <xs:element ref="library_physics_scenes">
                        <xs:annotation>
                            <xs:documentation>
                            The COLLADA element may contain any number of library_physics_scenes elements.
                            </xs:documentation>
                        </xs:annotation>
                    </xs:element>
                    <xs:element ref="library_visual_scenes">
                        <xs:annotation>
                            <xs:documentation>
                            The COLLADA element may contain any number of library_visual_scenes elements.
                            </xs:documentation>
                        </xs:annotation>
                    </xs:element>
                </xs:choice>
                <xs:element name="scene" minOccurs="0">
                    <xs:annotation>
                        <xs:documentation>
                        The scene embodies the entire set of information that can be visualized from the
                        contents of a COLLADA resource. The scene element declares the base of the scene
                        hierarchy or scene graph. The scene contains elements that comprise much of the
                        visual and transformational information content as created by the authoring tools.
                        </xs:documentation>
                    </xs:annotation>
                    <xs:complexType>
                        <xs:sequence>
                            <xs:element name="instance_physics_scene" type="InstanceWithExtra" minOccurs="0" maxOccurs="unbounded">
                                <xs:annotation>
                                    <xs:documentation>
                                    The instance_physics_scene element declares the instantiation of a COLLADA physics_scene resource.
                                    The instance_physics_scene element may appear any number of times.
                                    </xs:documentation>
                                </xs:annotation>
                            </xs:element>
                            <xs:element name="instance_visual_scene" type="InstanceWithExtra" minOccurs="0">
                                <xs:annotation>
                                    <xs:documentation>
                                    The instance_visual_scene element declares the instantiation of a COLLADA visual_scene resource.
                                    The instance_visual_scene element may only appear once.
                                    </xs:documentation>
                                </xs:annotation>
                            </xs:element>
                            <xs:element ref="extra" minOccurs="0" maxOccurs="unbounded">
                                <xs:annotation>
                                    <xs:documentation>
                                    The extra element may appear any number of times.
                                    </xs:documentation>
                                </xs:annotation>
                            </xs:element>
                        </xs:sequence>
                    </xs:complexType>
                </xs:element>
                <xs:element ref="extra" minOccurs="0" maxOccurs="unbounded">
                    <xs:annotation>
                        <xs:documentation>
                        The extra element may appear any number of times.
                        </xs:documentation>
                    </xs:annotation>
                </xs:element>
            </xs:sequence>
            <xs:attribute name="version" type="VersionType" use="required">
                <xs:annotation>
                    <xs:documentation>
                        The version attribute is the COLLADA schema revision with which the instance document
                        conforms. Required Attribute.
                    </xs:documentation>
                </xs:annotation>
            </xs:attribute>
            <xs:attribute ref="xml:base">
                <xs:annotation>
                    <xs:documentation>
                    The xml:base attribute allows you to define the base URI for this COLLADA document. See
                    http://www.w3.org/TR/xmlbase/ for more information.
                    </xs:documentation>
                </xs:annotation>
            </xs:attribute>
        </xs:complexType>
    </xs:element>
    <!-- Simple Types -->
    <!-- Primitive Types -->
    <xs:simpleType name="bool">
        <xs:restriction base="xs:boolean"/>
    </xs:simpleType>
    <xs:simpleType name="dateTime">
        <xs:restriction base="xs:dateTime"/>
    </xs:simpleType>
    <xs:simpleType name="float">
        <xs:restriction base="xs:double"/>
    </xs:simpleType>
    <xs:simpleType name="int">
        <xs:restriction base="xs:long"/>
    </xs:simpleType>
    <xs:simpleType name="Name">
        <xs:restriction base="xs:Name"/>
    </xs:simpleType>
    <xs:simpleType name="string">
        <xs:restriction base="xs:string"/>
    </xs:simpleType>
    <xs:simpleType name="token">
        <xs:restriction base="xs:token"/>
    </xs:simpleType>
    <xs:simpleType name="uint">
        <xs:restriction base="xs:unsignedLong"/>
    </xs:simpleType>
    <!-- Container Types -->
    <xs:simpleType name="ListOfBools">
        <xs:list itemType="bool"/>
    </xs:simpleType>
    <xs:simpleType name="ListOfFloats">
        <xs:list itemType="float"/>
    </xs:simpleType>
    <xs:simpleType name="ListOfHexBinary">
        <xs:list itemType="xs:hexBinary"/>
    </xs:simpleType>
    <xs:simpleType name="ListOfInts">
        <xs:list itemType="int"/>
    </xs:simpleType>
    <xs:simpleType name="ListOfNames">
        <xs:list itemType="Name"/>
    </xs:simpleType>
    <xs:simpleType name="ListOfTokens">
        <xs:list itemType="token"/>
    </xs:simpleType>
    <xs:simpleType name="ListOfUInts">
        <xs:list itemType="uint"/>
    </xs:simpleType>
    <!-- Aggregate Types -->
    <xs:simpleType name="bool2">
        <xs:restriction base="ListOfBools">
            <xs:minLength value="2"/>
            <xs:maxLength value="2"/>
        </xs:restriction>
    </xs:simpleType>
    <xs:simpleType name="bool3">
        <xs:restriction base="ListOfBools">
            <xs:minLength value="3"/>
            <xs:maxLength value="3"/>
        </xs:restriction>
    </xs:simpleType>
    <xs:simpleType name="bool4">
        <xs:restriction base="ListOfBools">
            <xs:minLength value="4"/>
            <xs:maxLength value="4"/>
        </xs:restriction>
    </xs:simpleType>
    <xs:simpleType name="float2">
        <xs:restriction base="ListOfFloats">
            <xs:minLength value="2"/>
            <xs:maxLength value="2"/>
        </xs:restriction>
    </xs:simpleType>
    <xs:simpleType name="float3">
        <xs:restriction base="ListOfFloats">
            <xs:minLength value="3"/>
            <xs:maxLength value="3"/>
        </xs:restriction>
    </xs:simpleType>
    <xs:simpleType name="float4">
        <xs:restriction base="ListOfFloats">
            <xs:minLength value="4"/>
            <xs:maxLength value="4"/>
        </xs:restriction>
    </xs:simpleType>
    <xs:simpleType name="float7">
        <xs:restriction base="ListOfFloats">
            <xs:minLength value="7"/>
            <xs:maxLength value="7"/>
        </xs:restriction>
    </xs:simpleType>
    <xs:simpleType name="float2x2">
        <xs:restriction base="ListOfFloats">
            <xs:minLength value="4"/>
            <xs:maxLength value="4"/>
        </xs:restriction>
    </xs:simpleType>
    <xs:simpleType name="float3x3">
        <xs:restriction base="ListOfFloats">
            <xs:minLength value="9"/>
            <xs:maxLength value="9"/>
        </xs:restriction>
    </xs:simpleType>
    <xs:simpleType name="float4x4">
        <xs:restriction base="ListOfFloats">
            <xs:minLength value="16"/>
            <xs:maxLength value="16"/>
        </xs:restriction>
    </xs:simpleType>
    <xs:simpleType name="float2x3">
        <xs:restriction base="ListOfFloats">
            <xs:minLength value="6"/>
            <xs:maxLength value="6"/>
        </xs:restriction>
    </xs:simpleType>
    <xs:simpleType name="float2x4">
        <xs:restriction base="ListOfFloats">
            <xs:minLength value="8"/>
            <xs:maxLength value="8"/>
        </xs:restriction>
    </xs:simpleType>
    <xs:simpleType name="float3x2">
        <xs:restriction base="ListOfFloats">
            <xs:minLength value="6"/>
            <xs:maxLength value="6"/>
        </xs:restriction>
    </xs:simpleType>
    <xs:simpleType name="float3x4">
        <xs:restriction base="ListOfFloats">
            <xs:minLength value="12"/>
            <xs:maxLength value="12"/>
        </xs:restriction>
    </xs:simpleType>
    <xs:simpleType name="float4x2">
        <xs:restriction base="ListOfFloats">
            <xs:minLength value="8"/>
            <xs:maxLength value="8"/>
        </xs:restriction>
    </xs:simpleType>
    <xs:simpleType name="float4x3">
        <xs:restriction base="ListOfFloats">
            <xs:minLength value="12"/>
            <xs:maxLength value="12"/>
        </xs:restriction>
    </xs:simpleType>
    <xs:simpleType name="int2">
        <xs:restriction base="ListOfInts">
            <xs:minLength value="2"/>
            <xs:maxLength value="2"/>
        </xs:restriction>
    </xs:simpleType>
    <xs:simpleType name="int3">
        <xs:restriction base="ListOfInts">
            <xs:minLength value="3"/>
            <xs:maxLength value="3"/>
        </xs:restriction>
    </xs:simpleType>
    <xs:simpleType name="int4">
        <xs:restriction base="ListOfInts">
            <xs:minLength value="4"/>
            <xs:maxLength value="4"/>
        </xs:restriction>
    </xs:simpleType>
    <xs:simpleType name="int2x2">
        <xs:restriction base="ListOfInts">
            <xs:minLength value="4"/>
            <xs:maxLength value="4"/>
        </xs:restriction>
    </xs:simpleType>
    <xs:simpleType name="int3x3">
        <xs:restriction base="ListOfInts">
            <xs:minLength value="9"/>
            <xs:maxLength value="9"/>
        </xs:restriction>
    </xs:simpleType>
    <xs:simpleType name="int4x4">
        <xs:restriction base="ListOfInts">
            <xs:minLength value="16"/>
            <xs:maxLength value="16"/>
        </xs:restriction>
    </xs:simpleType>
    <!-- Basic Enumerations -->
    <xs:simpleType name="MorphMethodType">
        <xs:annotation>
            <xs:documentation>
            An enumuerated type specifying the acceptable morph methods.
            </xs:documentation>
        </xs:annotation>
        <xs:restriction base="xs:string">
            <xs:enumeration value="NORMALIZED"/>
            <xs:enumeration value="RELATIVE"/>
        </xs:restriction>
    </xs:simpleType>
    <xs:simpleType name="NodeType">
        <xs:annotation>
            <xs:documentation>
            An enumerated type specifying the acceptable node types.
            </xs:documentation>
        </xs:annotation>
        <xs:restriction base="xs:string">
            <xs:enumeration value="JOINT"/>
            <xs:enumeration value="NODE"/>
        </xs:restriction>
    </xs:simpleType>
    <xs:simpleType name="URIFragmentType">
        <xs:annotation>
            <xs:documentation>
            This type is used for URI reference which can only reference a resource declared within it's same document.
            </xs:documentation>
        </xs:annotation>
        <xs:restriction base="xs:string">
            <xs:pattern value="(#(.*))"/>
        </xs:restriction>
    </xs:simpleType>
    <xs:simpleType name="UpAxisType">
        <xs:annotation>
            <xs:documentation>
            An enumerated type specifying the acceptable up-axis values.
            </xs:documentation>
        </xs:annotation>
        <xs:restriction base="xs:string">
            <xs:enumeration value="X_UP"/>
            <xs:enumeration value="Y_UP"/>
            <xs:enumeration value="Z_UP"/>
        </xs:restriction>
    </xs:simpleType>
    <xs:simpleType name="VersionType">
        <xs:annotation>
            <xs:documentation>
            An enumerated type specifying the acceptable document versions.
            </xs:documentation>
        </xs:annotation>
        <xs:restriction base="xs:string">
            <xs:enumeration value="1.4.0"/>
            <xs:enumeration value="1.4.1"/>
        </xs:restriction>
    </xs:simpleType>
    <!-- Complex Types -->
    <xs:complexType name="InputGlobal">
        <xs:annotation>
            <xs:documentation>
            The InputGlobal type is used to represent inputs that can reference external resources.
            </xs:documentation>
        </xs:annotation>
        <xs:attribute name="semantic" type="xs:NMTOKEN" use="required">
            <xs:annotation>
                <xs:documentation>
                The semantic attribute is the user-defined meaning of the input connection. Required attribute.
                </xs:documentation>
            </xs:annotation>
        </xs:attribute>
        <xs:attribute name="source" type="xs:anyURI" use="required">
            <xs:annotation>
                <xs:documentation>
                The source attribute indicates the location of the data source. Required attribute.
                </xs:documentation>
            </xs:annotation>
        </xs:attribute>
    </xs:complexType>
    <xs:complexType name="InputLocal">
        <xs:annotation>
            <xs:documentation>
            The InputLocal type is used to represent inputs that can only reference resources declared in the same document.
            </xs:documentation>
        </xs:annotation>
        <xs:attribute name="semantic" type="xs:NMTOKEN" use="required">
            <xs:annotation>
                <xs:documentation>
                The semantic attribute is the user-defined meaning of the input connection. Required attribute.
                </xs:documentation>
            </xs:annotation>
        </xs:attribute>
        <xs:attribute name="source" type="URIFragmentType" use="required">
            <xs:annotation>
                <xs:documentation>
                The source attribute indicates the location of the data source. Required attribute.
                </xs:documentation>
            </xs:annotation>
        </xs:attribute>
    </xs:complexType>
    <xs:complexType name="InputLocalOffset">
        <xs:annotation>
            <xs:documentation>
            The InputLocalOffset type is used to represent indexed inputs that can only reference resources declared in the same document.
            </xs:documentation>
        </xs:annotation>
        <xs:attribute name="offset" type="uint" use="required">
            <xs:annotation>
                <xs:documentation>
                The offset attribute represents the offset into the list of indices.  If two input elements share
                the same offset, they will be indexed the same.  This works as a simple form of compression for the
                list of indices as well as defining the order the inputs should be used in.  Required attribute.
                </xs:documentation>
            </xs:annotation>
        </xs:attribute>
        <xs:attribute name="semantic" type="xs:NMTOKEN" use="required">
            <xs:annotation>
                <xs:documentation>
                The semantic attribute is the user-defined meaning of the input connection. Required attribute.
                </xs:documentation>
            </xs:annotation>
        </xs:attribute>
        <xs:attribute name="source" type="URIFragmentType" use="required">
            <xs:annotation>
                <xs:documentation>
                The source attribute indicates the location of the data source. Required attribute.
                </xs:documentation>
            </xs:annotation>
        </xs:attribute>
        <xs:attribute name="set" type="uint">
            <xs:annotation>
                <xs:documentation>
                The set attribute indicates which inputs should be grouped together as a single set. This is helpful
                when multiple inputs share the same semantics.
                </xs:documentation>
            </xs:annotation>
        </xs:attribute>
    </xs:complexType>
    <xs:complexType name="InstanceWithExtra">
        <xs:annotation>
            <xs:documentation>
            The InstanceWithExtra type is used for all generic instance elements. A generic instance element
            is one which does not have any specific child elements declared.
            </xs:documentation>
        </xs:annotation>
        <xs:sequence>
            <xs:element ref="extra" minOccurs="0" maxOccurs="unbounded">
                <xs:annotation>
                    <xs:documentation>
                    The extra element may occur any number of times.
                    </xs:documentation>
                </xs:annotation>
            </xs:element>
        </xs:sequence>
        <xs:attribute name="url" type="xs:anyURI" use="required">
            <xs:annotation>
                <xs:documentation>
                The url attribute refers to resource to instantiate. This may refer to a local resource using a
                relative URL fragment identifier that begins with the “#” character. The url attribute may refer
                to an external resource using an absolute or relative URL.
                </xs:documentation>
            </xs:annotation>
        </xs:attribute>
        <xs:attribute name="sid" type="xs:NCName">
            <xs:annotation>
                <xs:documentation>
                The sid attribute is a text string value containing the sub-identifier of this element. This
                value must be unique within the scope of the parent element. Optional attribute.
                </xs:documentation>
            </xs:annotation>
        </xs:attribute>
        <xs:attribute name="name" type="xs:NCName">
            <xs:annotation>
                <xs:documentation>
                The name attribute is the text string name of this element. Optional attribute.
                </xs:documentation>
            </xs:annotation>
        </xs:attribute>
    </xs:complexType>
    <xs:complexType name="TargetableFloat">
        <xs:annotation>
            <xs:documentation>
            The TargetableFloat type is used to represent elements which contain a single float value which can
            be targeted for animation.
            </xs:documentation>
        </xs:annotation>
        <xs:simpleContent>
            <xs:extension base="float">
                <xs:attribute name="sid" type="xs:NCName">
                    <xs:annotation>
                        <xs:documentation>
                        The sid attribute is a text string value containing the sub-identifier of this element. This
                        value must be unique within the scope of the parent element. Optional attribute.
                        </xs:documentation>
                    </xs:annotation>
                </xs:attribute>
            </xs:extension>
        </xs:simpleContent>
    </xs:complexType>
    <xs:complexType name="TargetableFloat3">
        <xs:annotation>
            <xs:documentation>
            The TargetableFloat3 type is used to represent elements which contain a float3 value which can
            be targeted for animation.
            </xs:documentation>
        </xs:annotation>
        <xs:simpleContent>
            <xs:extension base="float3">
                <xs:attribute name="sid" type="xs:NCName">
                    <xs:annotation>
                        <xs:documentation>
                        The sid attribute is a text string value containing the sub-identifier of this element.
                        This value must be unique within the scope of the parent element. Optional attribute.
                        </xs:documentation>
                    </xs:annotation>
                </xs:attribute>
            </xs:extension>
        </xs:simpleContent>
    </xs:complexType>
    <!--Typed Array Elements-->
    <xs:element name="IDREF_array">
        <xs:annotation>
            <xs:documentation>
            The IDREF_array element declares the storage for a homogenous array of ID reference values.
            </xs:documentation>
        </xs:annotation>
        <xs:complexType>
            <xs:simpleContent>
                <xs:extension base="xs:IDREFS">
                    <xs:attribute name="id" type="xs:ID">
                        <xs:annotation>
                            <xs:documentation>
                            The id attribute is a text string containing the unique identifier of this element. This value
                            must be unique within the instance document. Optional attribute.
                            </xs:documentation>
                        </xs:annotation>
                    </xs:attribute>
                    <xs:attribute name="name" type="xs:NCName">
                        <xs:annotation>
                            <xs:documentation>
                            The name attribute is the text string name of this element. Optional attribute.
                            </xs:documentation>
                        </xs:annotation>
                    </xs:attribute>
                    <xs:attribute name="count" type="uint" use="required">
                        <xs:annotation>
                            <xs:documentation>
                            The count attribute indicates the number of values in the array. Required attribute.
                            </xs:documentation>
                        </xs:annotation>
                    </xs:attribute>
                </xs:extension>
            </xs:simpleContent>
        </xs:complexType>
    </xs:element>
    <xs:element name="Name_array">
        <xs:annotation>
            <xs:documentation>
            The Name_array element declares the storage for a homogenous array of Name string values.
            </xs:documentation>
        </xs:annotation>
        <xs:complexType>
            <xs:simpleContent>
                <xs:extension base="ListOfNames">
                    <xs:attribute name="id" type="xs:ID">
                        <xs:annotation>
                            <xs:documentation>
                            The id attribute is a text string containing the unique identifier of this element.
                            This value must be unique within the instance document. Optional attribute.
                            </xs:documentation>
                        </xs:annotation>
                    </xs:attribute>
                    <xs:attribute name="name" type="xs:NCName">
                        <xs:annotation>
                            <xs:documentation>
                            The name attribute is the text string name of this element. Optional attribute.
                            </xs:documentation>
                        </xs:annotation>
                    </xs:attribute>
                    <xs:attribute name="count" type="uint" use="required">
                        <xs:annotation>
                            <xs:documentation>
                            The count attribute indicates the number of values in the array. Required attribute.
                            </xs:documentation>
                        </xs:annotation>
                    </xs:attribute>
                </xs:extension>
            </xs:simpleContent>
        </xs:complexType>
    </xs:element>
    <xs:element name="bool_array">
        <xs:annotation>
            <xs:documentation>
            The bool_array element declares the storage for a homogenous array of boolean values.
            </xs:documentation>
        </xs:annotation>
        <xs:complexType>
            <xs:simpleContent>
                <xs:extension base="ListOfBools">
                    <xs:attribute name="id" type="xs:ID">
                        <xs:annotation>
                            <xs:documentation>
                            The id attribute is a text string containing the unique identifier of this element.
                            This value must be unique within the instance document. Optional attribute.
                            </xs:documentation>
                        </xs:annotation>
                    </xs:attribute>
                    <xs:attribute name="name" type="xs:NCName">
                        <xs:annotation>
                            <xs:documentation>
                            The name attribute is the text string name of this element. Optional attribute.
                            </xs:documentation>
                        </xs:annotation>
                    </xs:attribute>
                    <xs:attribute name="count" type="uint" use="required">
                        <xs:annotation>
                            <xs:documentation>
                            The count attribute indicates the number of values in the array. Required attribute.
                            </xs:documentation>
                        </xs:annotation>
                    </xs:attribute>
                </xs:extension>
            </xs:simpleContent>
        </xs:complexType>
    </xs:element>
    <xs:element name="float_array">
        <xs:annotation>
            <xs:documentation>
            The float_array element declares the storage for a homogenous array of floating point values.
            </xs:documentation>
        </xs:annotation>
        <xs:complexType>
            <xs:simpleContent>
                <xs:extension base="ListOfFloats">
                    <xs:attribute name="id" type="xs:ID">
                        <xs:annotation>
                            <xs:documentation>
                            The id attribute is a text string containing the unique identifier of this element. This value
                            must be unique within the instance document. Optional attribute.
                            </xs:documentation>
                        </xs:annotation>
                    </xs:attribute>
                    <xs:attribute name="name" type="xs:NCName">
                        <xs:annotation>
                            <xs:documentation>
                            The name attribute is the text string name of this element. Optional attribute.
                            </xs:documentation>
                        </xs:annotation>
                    </xs:attribute>
                    <xs:attribute name="count" type="uint" use="required">
                        <xs:annotation>
                            <xs:documentation>
                            The count attribute indicates the number of values in the array. Required attribute.
                            </xs:documentation>
                        </xs:annotation>
                    </xs:attribute>
                    <xs:attribute name="digits" type="xs:short" default="6">
                        <xs:annotation>
                            <xs:documentation>
                            The digits attribute indicates the number of significant decimal digits of the float values that
                            can be contained in the array. The default value is 6. Optional attribute.
                            </xs:documentation>
                        </xs:annotation>
                    </xs:attribute>
                    <xs:attribute name="magnitude" type="xs:short" default="38">
                        <xs:annotation>
                            <xs:documentation>
                            The magnitude attribute indicates the largest exponent of the float values that can be contained
                            in the array. The default value is 38. Optional attribute.
                            </xs:documentation>
                        </xs:annotation>
                    </xs:attribute>
                </xs:extension>
            </xs:simpleContent>
        </xs:complexType>
    </xs:element>
    <xs:element name="int_array">
        <xs:annotation>
            <xs:documentation>
            The int_array element declares the storage for a homogenous array of integer values.
            </xs:documentation>
        </xs:annotation>
        <xs:complexType>
            <xs:simpleContent>
                <xs:extension base="ListOfInts">
                    <xs:attribute name="id" type="xs:ID">
                        <xs:annotation>
                            <xs:documentation>
                            The id attribute is a text string containing the unique identifier of this element.
                            This value must be unique within the instance document. Optional attribute.
                            </xs:documentation>
                        </xs:annotation>
                    </xs:attribute>
                    <xs:attribute name="name" type="xs:NCName">
                        <xs:annotation>
                            <xs:documentation>
                            The name attribute is the text string name of this element. Optional attribute.
                            </xs:documentation>
                        </xs:annotation>
                    </xs:attribute>
                    <xs:attribute name="count" type="uint" use="required">
                        <xs:annotation>
                            <xs:documentation>
                            The count attribute indicates the number of values in the array. Required attribute.
                            </xs:documentation>
                        </xs:annotation>
                    </xs:attribute>
                    <xs:attribute name="minInclusive" type="xs:integer" default="-2147483648">
                        <xs:annotation>
                            <xs:documentation>
                            The minInclusive attribute indicates the smallest integer value that can be contained in
                            the array. The default value is –2147483648. Optional attribute.
                            </xs:documentation>
                        </xs:annotation>
                    </xs:attribute>
                    <xs:attribute name="maxInclusive" type="xs:integer" default="2147483647">
                        <xs:annotation>
                            <xs:documentation>
                            The maxInclusive attribute indicates the largest integer value that can be contained in
                            the array. The default value is 2147483647. Optional attribute.
                            </xs:documentation>
                        </xs:annotation>
                    </xs:attribute>
                </xs:extension>
            </xs:simpleContent>
        </xs:complexType>
    </xs:element>
    <!-- Dataflow Elements -->
    <xs:element name="accessor">
        <xs:annotation>
            <xs:documentation>
            The accessor element declares an access pattern to one of the array elements: float_array,
            int_array, Name_array, bool_array, and IDREF_array. The accessor element describes access
            to arrays that are organized in either an interleaved or non-interleaved manner, depending
            on the offset and stride attributes.
            </xs:documentation>
        </xs:annotation>
        <xs:complexType>
            <xs:sequence>
                <xs:element ref="param" minOccurs="0" maxOccurs="unbounded">
                    <xs:annotation>
                        <xs:documentation>
                        The accessor element may have any number of param elements.
                        </xs:documentation>
                    </xs:annotation>
                </xs:element>
            </xs:sequence>
            <xs:attribute name="count" type="uint" use="required">
                <xs:annotation>
                    <xs:documentation>
                    The count attribute indicates the number of times the array is accessed. Required attribute.
                    </xs:documentation>
                </xs:annotation>
            </xs:attribute>
            <xs:attribute name="offset" type="uint" default="0">
                <xs:annotation>
                    <xs:documentation>
                    The offset attribute indicates the index of the first value to be read from the array.
                    The default value is 0. Optional attribute.
                    </xs:documentation>
                </xs:annotation>
            </xs:attribute>
            <xs:attribute name="source" type="xs:anyURI">
                <xs:annotation>
                    <xs:documentation>
                    The source attribute indicates the location of the array to access using a URL expression. Required attribute.
                    </xs:documentation>
                </xs:annotation>
            </xs:attribute>
            <xs:attribute name="stride" type="uint" default="1">
                <xs:annotation>
                    <xs:documentation>
                    The stride attribute indicates number of values to be considered a unit during each access to
                    the array. The default value is 1, indicating that a single value is accessed. Optional attribute.
                    </xs:documentation>
                </xs:annotation>
            </xs:attribute>
        </xs:complexType>
    </xs:element>
    <xs:element name="param">
        <xs:annotation>
            <xs:documentation>
            The param element declares parametric information regarding its parent element.
            </xs:documentation>
        </xs:annotation>
        <xs:complexType>
            <xs:simpleContent>
                <xs:extension base="xs:string">
                    <xs:attribute name="name" type="xs:NCName">
                        <xs:annotation>
                            <xs:documentation>
                            The name attribute is the text string name of this element. Optional attribute.
                            </xs:documentation>
                        </xs:annotation>
                    </xs:attribute>
                    <xs:attribute name="sid" type="xs:NCName">
                        <xs:annotation>
                            <xs:documentation>
                            The sid attribute is a text string value containing the sub-identifier of this element.
                            This value must be unique within the scope of the parent element. Optional attribute.
                            </xs:documentation>
                        </xs:annotation>
                    </xs:attribute>
                    <xs:attribute name="semantic" type="xs:NMTOKEN">
                        <xs:annotation>
                            <xs:documentation>
                            The semantic attribute is the user-defined meaning of the parameter. Optional attribute.
                            </xs:documentation>
                        </xs:annotation>
                    </xs:attribute>
                    <xs:attribute name="type" type="xs:NMTOKEN" use="required">
                        <xs:annotation>
                            <xs:documentation>
                            The type attribute indicates the type of the value data. This text string must be understood
                            by the application. Required attribute.
                            </xs:documentation>
                        </xs:annotation>
                    </xs:attribute>
                </xs:extension>
            </xs:simpleContent>
        </xs:complexType>
    </xs:element>
    <xs:element name="source">
        <xs:annotation>
            <xs:documentation>
            The source element declares a data repository that provides values according to the semantics of an
            input element that refers to it.
            </xs:documentation>
        </xs:annotation>
        <xs:complexType>
            <xs:sequence>
                <xs:element ref="asset" minOccurs="0">
                    <xs:annotation>
                        <xs:documentation>
                        The source element may contain an asset element.
                        </xs:documentation>
                    </xs:annotation>
                </xs:element>
                <xs:choice minOccurs="0">
                    <xs:element ref="IDREF_array">
                        <xs:annotation>
                            <xs:documentation>
                            The source element may contain an IDREF_array.
                            </xs:documentation>
                        </xs:annotation>
                    </xs:element>
                    <xs:element ref="Name_array">
                        <xs:annotation>
                            <xs:documentation>
                            The source element may contain a Name_array.
                            </xs:documentation>
                        </xs:annotation>
                    </xs:element>
                    <xs:element ref="bool_array">
                        <xs:annotation>
                            <xs:documentation>
                            The source element may contain a bool_array.
                            </xs:documentation>
                        </xs:annotation>
                    </xs:element>
                    <xs:element ref="float_array">
                        <xs:annotation>
                            <xs:documentation>
                            The source element may contain a float_array.
                            </xs:documentation>
                        </xs:annotation>
                    </xs:element>
                    <xs:element ref="int_array">
                        <xs:annotation>
                            <xs:documentation>
                            The source element may contain an int_array.
                            </xs:documentation>
                        </xs:annotation>
                    </xs:element>
                </xs:choice>
                <xs:element name="technique_common" minOccurs="0">
                    <xs:annotation>
                        <xs:documentation>
                        The technique common specifies the common method for accessing this source element's data.
                        </xs:documentation>
                    </xs:annotation>
                    <xs:complexType>
                        <xs:sequence>
                            <xs:element ref="accessor">
                                <xs:annotation>
                                    <xs:documentation>
                                    The source's technique_common must have one and only one accessor.
                                    </xs:documentation>
                                </xs:annotation>
                            </xs:element>
                        </xs:sequence>
                    </xs:complexType>
                </xs:element>
                <xs:element ref="technique" minOccurs="0" maxOccurs="unbounded">
                    <xs:annotation>
                        <xs:documentation>
                        This element may contain any number of non-common profile techniques.
                        </xs:documentation>
                    </xs:annotation>
                </xs:element>
            </xs:sequence>
            <xs:attribute name="id" type="xs:ID" use="required">
                <xs:annotation>
                    <xs:documentation>
                    The id attribute is a text string containing the unique identifier of this element.
                    This value must be unique within the instance document. Required attribute.
                    </xs:documentation>
                </xs:annotation>
            </xs:attribute>
            <xs:attribute name="name" type="xs:NCName">
                <xs:annotation>
                    <xs:documentation>
                    The name attribute is the text string name of this element. Optional attribute.
                    </xs:documentation>
                </xs:annotation>
            </xs:attribute>
        </xs:complexType>
    </xs:element>
    <!-- Geometry Elements -->
    <xs:element name="geometry">
        <xs:annotation>
            <xs:documentation>
            Geometry describes the visual shape and appearance of an object in the scene.
            The geometry element categorizes the declaration of geometric information. Geometry is a
            branch of mathematics that deals with the measurement, properties, and relationships of
            points, lines, angles, surfaces, and solids.
            </xs:documentation>
        </xs:annotation>
        <xs:complexType>
            <xs:sequence>
                <xs:element ref="asset" minOccurs="0">
                    <xs:annotation>
                        <xs:documentation>
                        The geometry element may contain an asset element.
                        </xs:documentation>
                    </xs:annotation>
                </xs:element>
                <xs:choice>
                    <xs:element ref="convex_mesh">
                        <xs:annotation>
                            <xs:documentation>
                            The geometry element may contain only one mesh or convex_mesh.
                            </xs:documentation>
                        </xs:annotation>
                    </xs:element>
                    <xs:element ref="mesh">
                        <xs:annotation>
                            <xs:documentation>
                            The geometry element may contain only one mesh or convex_mesh.
                            </xs:documentation>
                        </xs:annotation>
                    </xs:element>
                    <xs:element ref="spline"/>
                </xs:choice>
                <xs:element ref="extra" minOccurs="0" maxOccurs="unbounded">
                    <xs:annotation>
                        <xs:documentation>
                        The extra element may appear any number of times.
                        </xs:documentation>
                    </xs:annotation>
                </xs:element>
            </xs:sequence>
            <xs:attribute name="id" type="xs:ID">
                <xs:annotation>
                    <xs:documentation>
                    The id attribute is a text string containing the unique identifier of this element.
                    This value must be unique within the instance document. Optional attribute.
                    </xs:documentation>
                </xs:annotation>
            </xs:attribute>
            <xs:attribute name="name" type="xs:NCName">
                <xs:annotation>
                    <xs:documentation>
                    The name attribute is the text string name of this element. Optional attribute.
                    </xs:documentation>
                </xs:annotation>
            </xs:attribute>
        </xs:complexType>
    </xs:element>
    <xs:element name="mesh">
        <xs:annotation>
            <xs:documentation>
            The mesh element contains vertex and primitive information sufficient to describe basic geometric meshes.
            </xs:documentation>
        </xs:annotation>
        <xs:complexType>
            <xs:sequence>
                <xs:element ref="source" maxOccurs="unbounded">
                    <xs:annotation>
                        <xs:documentation>
                        The mesh element must contain one or more source elements.
                        </xs:documentation>
                    </xs:annotation>
                </xs:element>
                <xs:element ref="vertices">
                    <xs:annotation>
                        <xs:documentation>
                        The mesh element must contain one vertices element.
                        </xs:documentation>
                    </xs:annotation>
                </xs:element>
                <xs:choice minOccurs="0" maxOccurs="unbounded">
                    <xs:element ref="lines">
                        <xs:annotation>
                            <xs:documentation>
                            The mesh element may contain any number of lines elements.
                            </xs:documentation>
                        </xs:annotation>
                    </xs:element>
                    <xs:element ref="linestrips">
                        <xs:annotation>
                            <xs:documentation>
                            The mesh element may contain any number of linestrips elements.
                            </xs:documentation>
                        </xs:annotation>
                    </xs:element>
                    <xs:element ref="polygons">
                        <xs:annotation>
                            <xs:documentation>
                            The mesh element may contain any number of polygons elements.
                            </xs:documentation>
                        </xs:annotation>
                    </xs:element>
                    <xs:element ref="polylist">
                        <xs:annotation>
                            <xs:documentation>
                            The mesh element may contain any number of polylist elements.
                            </xs:documentation>
                        </xs:annotation>
                    </xs:element>
                    <xs:element ref="triangles">
                        <xs:annotation>
                            <xs:documentation>
                            The mesh element may contain any number of triangles elements.
                            </xs:documentation>
                        </xs:annotation>
                    </xs:element>
                    <xs:element ref="trifans">
                        <xs:annotation>
                            <xs:documentation>
                            The mesh element may contain any number of trifans elements.
                            </xs:documentation>
                        </xs:annotation>
                    </xs:element>
                    <xs:element ref="tristrips">
                        <xs:annotation>
                            <xs:documentation>
                            The mesh element may contain any number of tristrips elements.
                            </xs:documentation>
                        </xs:annotation>
                    </xs:element>
                </xs:choice>
                <xs:element ref="extra" minOccurs="0" maxOccurs="unbounded">
                    <xs:annotation>
                        <xs:documentation>
                        The extra element may appear any number of times.
                        </xs:documentation>
                    </xs:annotation>
                </xs:element>
            </xs:sequence>
        </xs:complexType>
    </xs:element>
    <xs:element name="spline">
        <xs:annotation>
            <xs:documentation>
            The spline element contains control vertex information sufficient to describe basic splines.
            </xs:documentation>
        </xs:annotation>
        <xs:complexType>
            <xs:sequence>
                <xs:element ref="source" maxOccurs="unbounded">
                    <xs:annotation>
                        <xs:documentation>
                        The mesh element must contain one or more source elements.
                        </xs:documentation>
                    </xs:annotation>
                </xs:element>
                <xs:element name="control_vertices">
                    <xs:annotation>
                        <xs:documentation>The control vertices element  must occur  exactly one time. It is used to describe the CVs of the spline.</xs:documentation>
                    </xs:annotation>
                    <xs:complexType>
                        <xs:sequence>
                            <xs:element name="input" type="InputLocal" maxOccurs="unbounded">
                                <xs:annotation>
                                    <xs:documentation>
                        The input element must occur at least one time. These inputs are local inputs.
                        </xs:documentation>
                                </xs:annotation>
                            </xs:element>
                            <xs:element ref="extra" minOccurs="0" maxOccurs="unbounded">
                                <xs:annotation>
                                    <xs:documentation>
                        The extra element may appear any number of times.
                        </xs:documentation>
                                </xs:annotation>
                            </xs:element>
                        </xs:sequence>
                    </xs:complexType>
                </xs:element>
                <xs:element ref="extra" minOccurs="0" maxOccurs="unbounded">
                    <xs:annotation>
                        <xs:documentation>
                        The extra element may appear any number of times.
                        </xs:documentation>
                    </xs:annotation>
                </xs:element>
            </xs:sequence>
            <xs:attribute name="closed" type="bool" default="false"/>
        </xs:complexType>
    </xs:element>
    <!-- Collation Elements -->
    <xs:element name="p" type="ListOfUInts">
        <xs:annotation>
            <xs:documentation>
            The p element represents primitive data for the primitive types (lines, linestrips, polygons,
            polylist, triangles, trifans, tristrips). The p element contains indices that reference into
            the parent's source elements referenced by the input elements.
            </xs:documentation>
        </xs:annotation>
    </xs:element>
    <xs:element name="lines">
        <xs:annotation>
            <xs:documentation>
            The lines element provides the information needed to bind vertex attributes together and then
            organize those vertices into individual lines. Each line described by the mesh has two vertices.
            The first line is formed from first and second vertices. The second line is formed from the
            third and fourth vertices and so on.
            </xs:documentation>
        </xs:annotation>
        <xs:complexType>
            <xs:sequence>
                <xs:element name="input" type="InputLocalOffset" minOccurs="0" maxOccurs="unbounded">
                    <xs:annotation>
                        <xs:documentation>
                        The input element may occur any number of times. This input is a local input with the offset
                        and set attributes.
                        </xs:documentation>
                    </xs:annotation>
                </xs:element>
                <xs:element ref="p" minOccurs="0">
                    <xs:annotation>
                        <xs:documentation>
                        The p element may occur once.
                        </xs:documentation>
                    </xs:annotation>
                </xs:element>
                <xs:element ref="extra" minOccurs="0" maxOccurs="unbounded">
                    <xs:annotation>
                        <xs:documentation>
                        The extra element may appear any number of times.
                        </xs:documentation>
                    </xs:annotation>
                </xs:element>
            </xs:sequence>
            <xs:attribute name="name" type="xs:NCName">
                <xs:annotation>
                    <xs:documentation>
                    The name attribute is the text string name of this element. Optional attribute.
                    </xs:documentation>
                </xs:annotation>
            </xs:attribute>
            <xs:attribute name="count" type="uint" use="required">
                <xs:annotation>
                    <xs:documentation>
                    The count attribute indicates the number of line primitives. Required attribute.
                    </xs:documentation>
                </xs:annotation>
            </xs:attribute>
            <xs:attribute name="material" type="xs:NCName">
                <xs:annotation>
                    <xs:documentation>
                    The material attribute declares a symbol for a material. This symbol is bound to a material at
                    the time of instantiation. If the material attribute is not specified then the lighting and
                    shading results are application defined. Optional attribute.
                    </xs:documentation>
                </xs:annotation>
            </xs:attribute>
        </xs:complexType>
    </xs:element>
    <xs:element name="linestrips">
        <xs:annotation>
            <xs:documentation>
            The linestrips element provides the information needed to bind vertex attributes together and
            then organize those vertices into connected line-strips. Each line-strip described by the mesh
            has an arbitrary number of vertices. Each line segment within the line-strip is formed from the
            current vertex and the preceding vertex.
            </xs:documentation>
        </xs:annotation>
        <xs:complexType>
            <xs:sequence>
                <xs:element name="input" type="InputLocalOffset" minOccurs="0" maxOccurs="unbounded">
                    <xs:annotation>
                        <xs:documentation>
                        The input element may occur any number of times. This input is a local input with the offset
                        and set attributes.
                        </xs:documentation>
                    </xs:annotation>
                </xs:element>
                <xs:element ref="p" minOccurs="0" maxOccurs="unbounded">
                    <xs:annotation>
                        <xs:documentation>
                        The linestrips element may have any number of p elements.
                        </xs:documentation>
                    </xs:annotation>
                </xs:element>
                <xs:element ref="extra" minOccurs="0" maxOccurs="unbounded">
                    <xs:annotation>
                        <xs:documentation>
                        The extra element may appear any number of times.
                        </xs:documentation>
                    </xs:annotation>
                </xs:element>
            </xs:sequence>
            <xs:attribute name="name" type="xs:NCName">
                <xs:annotation>
                    <xs:documentation>
                    The name attribute is the text string name of this element. Optional attribute.
                    </xs:documentation>
                </xs:annotation>
            </xs:attribute>
            <xs:attribute name="count" type="uint" use="required">
                <xs:annotation>
                    <xs:documentation>
                    The count attribute indicates the number of linestrip primitives. Required attribute.
                    </xs:documentation>
                </xs:annotation>
            </xs:attribute>
            <xs:attribute name="material" type="xs:NCName">
                <xs:annotation>
                    <xs:documentation>
                    The material attribute declares a symbol for a material. This symbol is bound to a material
                    at the time of instantiation. If the material attribute is not specified then the lighting
                    and shading results are application defined. Optional attribute.
                    </xs:documentation>
                </xs:annotation>
            </xs:attribute>
        </xs:complexType>
    </xs:element>
    <xs:element name="polygons">
        <xs:annotation>
            <xs:documentation>
            The polygons element provides the information needed to bind vertex attributes together and
            then organize those vertices into individual polygons. The polygons described can contain
            arbitrary numbers of vertices. These polygons may be self intersecting and may also contain holes.
            </xs:documentation>
        </xs:annotation>
        <xs:complexType>
            <xs:sequence>
                <xs:element name="input" type="InputLocalOffset" minOccurs="0" maxOccurs="unbounded">
                    <xs:annotation>
                        <xs:documentation>
                        The input element may occur any number of times. This input is a local input with the
                        offset and set attributes.
                        </xs:documentation>
                    </xs:annotation>
                </xs:element>
                <xs:choice minOccurs="0" maxOccurs="unbounded">
                    <xs:element ref="p">
                        <xs:annotation>
                            <xs:documentation>
                            The p element may occur any number of times.
                            </xs:documentation>
                        </xs:annotation>
                    </xs:element>
                    <xs:element name="ph">
                        <xs:annotation>
                            <xs:documentation>
                            The ph element descripes a polygon with holes.
                            </xs:documentation>
                        </xs:annotation>
                        <xs:complexType>
                            <xs:sequence>
                                <xs:element ref="p">
                                    <xs:annotation>
                                        <xs:documentation>
                                        Theere may only be one p element.
                                        </xs:documentation>
                                    </xs:annotation>
                                </xs:element>
                                <xs:element name="h" type="ListOfUInts" maxOccurs="unbounded">
                                    <xs:annotation>
                                        <xs:documentation>
                                        The h element represents a hole in the polygon specified. There must be at least one h element.
                                        </xs:documentation>
                                    </xs:annotation>
                                </xs:element>
                            </xs:sequence>
                        </xs:complexType>
                    </xs:element>
                </xs:choice>
                <xs:element ref="extra" minOccurs="0" maxOccurs="unbounded">
                    <xs:annotation>
                        <xs:documentation>
                        The extra element may appear any number of times.
                        </xs:documentation>
                    </xs:annotation>
                </xs:element>
            </xs:sequence>
            <xs:attribute name="name" type="xs:NCName">
                <xs:annotation>
                    <xs:documentation>
                    The name attribute is the text string name of this element. Optional attribute.
                    </xs:documentation>
                </xs:annotation>
            </xs:attribute>
            <xs:attribute name="count" type="uint" use="required">
                <xs:annotation>
                    <xs:documentation>
                    The count attribute indicates the number of polygon primitives. Required attribute.
                    </xs:documentation>
                </xs:annotation>
            </xs:attribute>
            <xs:attribute name="material" type="xs:NCName">
                <xs:annotation>
                    <xs:documentation>
                    The material attribute declares a symbol for a material. This symbol is bound to a material
                    at the time of instantiation. If the material attribute is not specified then the lighting
                    and shading results are application defined. Optional attribute.
                    </xs:documentation>
                </xs:annotation>
            </xs:attribute>
        </xs:complexType>
    </xs:element>
    <xs:element name="polylist">
        <xs:annotation>
            <xs:documentation>
            The polylist element provides the information needed to bind vertex attributes together and
            then organize those vertices into individual polygons. The polygons described in polylist can
            contain arbitrary numbers of vertices. Unlike the polygons element, the polylist element cannot
            contain polygons with holes.
            </xs:documentation>
        </xs:annotation>
        <xs:complexType>
            <xs:sequence>
                <xs:element name="input" type="InputLocalOffset" minOccurs="0" maxOccurs="unbounded">
                    <xs:annotation>
                        <xs:documentation>
                        The input element may occur any number of times. This input is a local input with the
                        offset and set attributes.
                        </xs:documentation>
                    </xs:annotation>
                </xs:element>
                <xs:element name="vcount" type="ListOfUInts" minOccurs="0">
                    <xs:annotation>
                        <xs:documentation>
                        The vcount element contains a list of integers describing the number of sides for each polygon
                        described by the polylist element. The vcount element may occur once.
                        </xs:documentation>
                    </xs:annotation>
                </xs:element>
                <xs:element ref="p" minOccurs="0">
                    <xs:annotation>
                        <xs:documentation>
                        The p element may occur once.
                        </xs:documentation>
                    </xs:annotation>
                </xs:element>
                <xs:element ref="extra" minOccurs="0" maxOccurs="unbounded">
                    <xs:annotation>
                        <xs:documentation>
                        The extra element may appear any number of times.
                        </xs:documentation>
                    </xs:annotation>
                </xs:element>
            </xs:sequence>
            <xs:attribute name="name" type="xs:NCName">
                <xs:annotation>
                    <xs:documentation>
                    The name attribute is the text string name of this element. Optional attribute.
                    </xs:documentation>
                </xs:annotation>
            </xs:attribute>
            <xs:attribute name="count" type="uint" use="required">
                <xs:annotation>
                    <xs:documentation>
                    The count attribute indicates the number of polygon primitives. Required attribute.
                    </xs:documentation>
                </xs:annotation>
            </xs:attribute>
            <xs:attribute name="material" type="xs:NCName">
                <xs:annotation>
                    <xs:documentation>
                    The material attribute declares a symbol for a material. This symbol is bound to a material at
                    the time of instantiation. If the material attribute is not specified then the lighting and
                    shading results are application defined. Optional attribute.
                    </xs:documentation>
                </xs:annotation>
            </xs:attribute>
        </xs:complexType>
    </xs:element>
    <xs:element name="triangles">
        <xs:annotation>
            <xs:documentation>
            The triangles element provides the information needed to bind vertex attributes together and
            then organize those vertices into individual triangles.    Each triangle described by the mesh has
            three vertices. The first triangle is formed from the first, second, and third vertices. The
            second triangle is formed from the fourth, fifth, and sixth vertices, and so on.
            </xs:documentation>
        </xs:annotation>
        <xs:complexType>
            <xs:sequence>
                <xs:element name="input" type="InputLocalOffset" minOccurs="0" maxOccurs="unbounded">
                    <xs:annotation>
                        <xs:documentation>
                        The input element may occur any number of times. This input is a local input with the
                        offset and set attributes.
                        </xs:documentation>
                    </xs:annotation>
                </xs:element>
                <xs:element ref="p" minOccurs="0">
                    <xs:annotation>
                        <xs:documentation>
                        The triangles element may have any number of p elements.
                        </xs:documentation>
                    </xs:annotation>
                </xs:element>
                <xs:element ref="extra" minOccurs="0" maxOccurs="unbounded">
                    <xs:annotation>
                        <xs:documentation>
                        The extra element may appear any number of times.
                        </xs:documentation>
                    </xs:annotation>
                </xs:element>
            </xs:sequence>
            <xs:attribute name="name" type="xs:NCName">
                <xs:annotation>
                    <xs:documentation>
                    The name attribute is the text string name of this element. Optional attribute.
                    </xs:documentation>
                </xs:annotation>
            </xs:attribute>
            <xs:attribute name="count" type="uint" use="required">
                <xs:annotation>
                    <xs:documentation>
                    The count attribute indicates the number of triangle primitives. Required attribute.
                    </xs:documentation>
                </xs:annotation>
            </xs:attribute>
            <xs:attribute name="material" type="xs:NCName">
                <xs:annotation>
                    <xs:documentation>
                    The material attribute declares a symbol for a material. This symbol is bound to a material at
                    the time of instantiation. Optional attribute. If the material attribute is not specified then
                    the lighting and shading results are application defined.
                    </xs:documentation>
                </xs:annotation>
            </xs:attribute>
        </xs:complexType>
    </xs:element>
    <xs:element name="trifans">
        <xs:annotation>
            <xs:documentation>
            The trifans element provides the information needed to bind vertex attributes together and then
            organize those vertices into connected triangles. Each triangle described by the mesh has three
            vertices. The first triangle is formed from first, second, and third vertices. Each subsequent
            triangle is formed from the current vertex, reusing the first and the previous vertices.
            </xs:documentation>
        </xs:annotation>
        <xs:complexType>
            <xs:sequence>
                <xs:element name="input" type="InputLocalOffset" minOccurs="0" maxOccurs="unbounded">
                    <xs:annotation>
                        <xs:documentation>
                        The input element may occur any number of times. This input is a local input with the
                        offset and set attributes.
                        </xs:documentation>
                    </xs:annotation>
                </xs:element>
                <xs:element ref="p" minOccurs="0" maxOccurs="unbounded">
                    <xs:annotation>
                        <xs:documentation>
                        The trifans element may have any number of p elements.
                        </xs:documentation>
                    </xs:annotation>
                </xs:element>
                <xs:element ref="extra" minOccurs="0" maxOccurs="unbounded">
                    <xs:annotation>
                        <xs:documentation>
                        The extra element may appear any number of times.
                        </xs:documentation>
                    </xs:annotation>
                </xs:element>
            </xs:sequence>
            <xs:attribute name="name" type="xs:NCName">
                <xs:annotation>
                    <xs:documentation>
                    The name attribute is the text string name of this element. Optional attribute.
                    </xs:documentation>
                </xs:annotation>
            </xs:attribute>
            <xs:attribute name="count" type="uint" use="required">
                <xs:annotation>
                    <xs:documentation>
                    The count attribute indicates the number of triangle fan primitives. Required attribute.
                    </xs:documentation>
                </xs:annotation>
            </xs:attribute>
            <xs:attribute name="material" type="xs:NCName">
                <xs:annotation>
                    <xs:documentation>
                    The material attribute declares a symbol for a material. This symbol is bound to a material
                    at the time of instantiation. If the material attribute is not specified then the lighting
                    and shading results are application defined. Optional attribute.
                    </xs:documentation>
                </xs:annotation>
            </xs:attribute>
        </xs:complexType>
    </xs:element>
    <xs:element name="tristrips">
        <xs:annotation>
            <xs:documentation>
            The tristrips element provides the information needed to bind vertex attributes together and then
            organize those vertices into connected triangles. Each triangle described by the mesh has three
            vertices. The first triangle is formed from first, second, and third vertices. Each subsequent
            triangle is formed from the current vertex, reusing the previous two vertices.
            </xs:documentation>
        </xs:annotation>
        <xs:complexType>
            <xs:sequence>
                <xs:element name="input" type="InputLocalOffset" minOccurs="0" maxOccurs="unbounded">
                    <xs:annotation>
                        <xs:documentation>
                        The input element may occur any number of times. This input is a local input with the offset
                        and set attributes.
                        </xs:documentation>
                    </xs:annotation>
                </xs:element>
                <xs:element ref="p" minOccurs="0" maxOccurs="unbounded">
                    <xs:annotation>
                        <xs:documentation>
                        The tristrips element may have any number of p elements.
                        </xs:documentation>
                    </xs:annotation>
                </xs:element>
                <xs:element ref="extra" minOccurs="0" maxOccurs="unbounded">
                    <xs:annotation>
                        <xs:documentation>
                        The extra element may appear any number of times.
                        </xs:documentation>
                    </xs:annotation>
                </xs:element>
            </xs:sequence>
            <xs:attribute name="name" type="xs:NCName">
                <xs:annotation>
                    <xs:documentation>
                    The name attribute is the text string name of this element. Optional attribute.
                    </xs:documentation>
                </xs:annotation>
            </xs:attribute>
            <xs:attribute name="count" type="uint" use="required">
                <xs:annotation>
                    <xs:documentation>
                    The count attribute indicates the number of triangle strip primitives. Required attribute.
                    </xs:documentation>
                </xs:annotation>
            </xs:attribute>
            <xs:attribute name="material" type="xs:NCName">
                <xs:annotation>
                    <xs:documentation>
                    The material attribute declares a symbol for a material. This symbol is bound to a material
                    at the time of instantiation. If the material attribute is not specified then the lighting
                    and shading results are application defined. Optional attribute.
                    </xs:documentation>
                </xs:annotation>
            </xs:attribute>
        </xs:complexType>
    </xs:element>
    <xs:element name="vertices">
        <xs:annotation>
            <xs:documentation>
            The vertices element declares the attributes and identity of mesh-vertices. The vertices element
            describes mesh-vertices in a mesh geometry. The mesh-vertices represent the position (identity)
            of the vertices comprising the mesh and other vertex attributes that are invariant to tessellation.
            </xs:documentation>
        </xs:annotation>
        <xs:complexType>
            <xs:sequence>
                <xs:element name="input" type="InputLocal" maxOccurs="unbounded">
                    <xs:annotation>
                        <xs:documentation>
                        The input element must occur at least one time. These inputs are local inputs.
                        </xs:documentation>
                    </xs:annotation>
                </xs:element>
                <xs:element ref="extra" minOccurs="0" maxOccurs="unbounded">
                    <xs:annotation>
                        <xs:documentation>
                        The extra element may appear any number of times.
                        </xs:documentation>
                    </xs:annotation>
                </xs:element>
            </xs:sequence>
            <xs:attribute name="id" type="xs:ID" use="required">
                <xs:annotation>
                    <xs:documentation>
                    The id attribute is a text string containing the unique identifier of this element. This
                    value must be unique within the instance document. Required attribute.
                    </xs:documentation>
                </xs:annotation>
            </xs:attribute>
            <xs:attribute name="name" type="xs:NCName">
                <xs:annotation>
                    <xs:documentation>
                    The name attribute is the text string name of this element. Optional attribute.
                    </xs:documentation>
                </xs:annotation>
            </xs:attribute>
        </xs:complexType>
    </xs:element>
    <!-- Transformational Elements -->
    <xs:element name="lookat">
        <xs:annotation>
            <xs:documentation>
            The lookat element contains a position and orientation transformation suitable for aiming a camera.
            The lookat element contains three mathematical vectors within it that describe:
            1.    The position of the object;
            2.    The position of the interest point;
            3.    The direction that points up.
            </xs:documentation>
        </xs:annotation>
        <xs:complexType>
            <xs:simpleContent>
                <xs:extension base="float3x3">
                    <xs:attribute name="sid" type="xs:NCName">
                        <xs:annotation>
                            <xs:documentation>
                            The sid attribute is a text string value containing the sub-identifier of this element.
                            This value must be unique within the scope of the parent element. Optional attribute.
                            </xs:documentation>
                        </xs:annotation>
                    </xs:attribute>
                </xs:extension>
            </xs:simpleContent>
        </xs:complexType>
    </xs:element>
    <xs:element name="matrix">
        <xs:annotation>
            <xs:documentation>
            Matrix transformations embody mathematical changes to points within a coordinate systems or the
            coordinate system itself. The matrix element contains a 4-by-4 matrix of floating-point values.
            </xs:documentation>
        </xs:annotation>
        <xs:complexType>
            <xs:simpleContent>
                <xs:extension base="float4x4">
                    <xs:attribute name="sid" type="xs:NCName">
                        <xs:annotation>
                            <xs:documentation>
                            The sid attribute is a text string value containing the sub-identifier of this element.
                            This value must be unique within the scope of the parent element. Optional attribute.
                            </xs:documentation>
                        </xs:annotation>
                    </xs:attribute>
                </xs:extension>
            </xs:simpleContent>
        </xs:complexType>
    </xs:element>
    <xs:element name="rotate">
        <xs:annotation>
            <xs:documentation>
            The rotate element contains an angle and a mathematical vector that represents the axis of rotation.
            </xs:documentation>
        </xs:annotation>
        <xs:complexType>
            <xs:simpleContent>
                <xs:extension base="float4">
                    <xs:attribute name="sid" type="xs:NCName">
                        <xs:annotation>
                            <xs:documentation>
                            The sid attribute is a text string value containing the sub-identifier of this element.
                            This value must be unique within the scope of the parent element. Optional attribute.
                            </xs:documentation>
                        </xs:annotation>
                    </xs:attribute>
                </xs:extension>
            </xs:simpleContent>
        </xs:complexType>
    </xs:element>
    <xs:element name="scale" type="TargetableFloat3">
        <xs:annotation>
            <xs:documentation>
            The scale element contains a mathematical vector that represents the relative proportions of the
            X, Y and Z axes of a coordinated system.
            </xs:documentation>
        </xs:annotation>
    </xs:element>
    <xs:element name="skew">
        <xs:annotation>
            <xs:documentation>
            The skew element contains an angle and two mathematical vectors that represent the axis of
            rotation and the axis of translation.
            </xs:documentation>
        </xs:annotation>
        <xs:complexType>
            <xs:simpleContent>
                <xs:extension base="float7">
                    <xs:attribute name="sid" type="xs:NCName">
                        <xs:annotation>
                            <xs:documentation>
                            The sid attribute is a text string value containing the sub-identifier of this element.
                            This value must be unique within the scope of the parent element. Optional attribute.
                            </xs:documentation>
                        </xs:annotation>
                    </xs:attribute>
                </xs:extension>
            </xs:simpleContent>
        </xs:complexType>
    </xs:element>
    <xs:element name="translate" type="TargetableFloat3">
        <xs:annotation>
            <xs:documentation>
            The translate element contains a mathematical vector that represents the distance along the
            X, Y and Z-axes.
            </xs:documentation>
        </xs:annotation>
    </xs:element>
    <!-- Lighting and Shading Elements -->
    <xs:element name="image">
        <xs:annotation>
            <xs:documentation>
            The image element declares the storage for the graphical representation of an object.
            The image element best describes raster image data, but can conceivably handle other
            forms of imagery. The image elements allows for specifying an external image file with
            the init_from element or embed image data with the data element.
            </xs:documentation>
        </xs:annotation>
        <xs:complexType>
            <xs:sequence>
                <xs:element ref="asset" minOccurs="0">
                    <xs:annotation>
                        <xs:documentation>
                        The image element may contain an asset element.
                        </xs:documentation>
                    </xs:annotation>
                </xs:element>
                <xs:choice>
                    <xs:element name="data" type="ListOfHexBinary">
                        <xs:annotation>
                            <xs:documentation>
                            The data child element contains a sequence of hexadecimal encoded  binary octets representing
                            the embedded image data.
                            </xs:documentation>
                        </xs:annotation>
                    </xs:element>
                    <xs:element name="init_from" type="xs:anyURI">
                        <xs:annotation>
                            <xs:documentation>
                            The init_from element allows you to specify an external image file to use for the image element.
                            </xs:documentation>
                        </xs:annotation>
                    </xs:element>
                </xs:choice>
                <xs:element ref="extra" minOccurs="0" maxOccurs="unbounded">
                    <xs:annotation>
                        <xs:documentation>
                        The extra element may appear any number of times.
                        </xs:documentation>
                    </xs:annotation>
                </xs:element>
            </xs:sequence>
            <xs:attribute name="id" type="xs:ID">
                <xs:annotation>
                    <xs:documentation>
                    The id attribute is a text string containing the unique identifier of this element. This value
                    must be unique within the instance document. Optional attribute.
                    </xs:documentation>
                </xs:annotation>
            </xs:attribute>
            <xs:attribute name="name" type="xs:NCName">
                <xs:annotation>
                    <xs:documentation>
                    The name attribute is the text string name of this element. Optional attribute.
                    </xs:documentation>
                </xs:annotation>
            </xs:attribute>
            <xs:attribute name="format" type="xs:token">
                <xs:annotation>
                    <xs:documentation>
                    The format attribute is a text string value that indicates the image format. Optional attribute.
                    </xs:documentation>
                </xs:annotation>
            </xs:attribute>
            <xs:attribute name="height" type="uint">
                <xs:annotation>
                    <xs:documentation>
                    The height attribute is an integer value that indicates the height of the image in pixel
                    units. Optional attribute.
                    </xs:documentation>
                </xs:annotation>
            </xs:attribute>
            <xs:attribute name="width" type="uint">
                <xs:annotation>
                    <xs:documentation>
                    The width attribute is an integer value that indicates the width of the image in pixel units.
                    Optional attribute.
                    </xs:documentation>
                </xs:annotation>
            </xs:attribute>
            <xs:attribute name="depth" type="uint" default="1">
                <xs:annotation>
                    <xs:documentation>
                    The depth attribute is an integer value that indicates the depth of the image in pixel units.
                    A 2-D image has a depth of 1, which is also the default value. Optional attribute.
                    </xs:documentation>
                </xs:annotation>
            </xs:attribute>
        </xs:complexType>
    </xs:element>
    <xs:element name="light">
        <xs:annotation>
            <xs:documentation>
            The light element declares a light source that illuminates the scene.
            Light sources have many different properties and radiate light in many different patterns and
            frequencies.
            </xs:documentation>
        </xs:annotation>
        <xs:complexType>
            <xs:sequence>
                <xs:element ref="asset" minOccurs="0">
                    <xs:annotation>
                        <xs:documentation>
                        The light element may contain an asset element.
                        </xs:documentation>
                    </xs:annotation>
                </xs:element>
                <xs:element name="technique_common">
                    <xs:annotation>
                        <xs:documentation>
                        The technique_common element specifies the light information for the common profile which all
                        COLLADA implementations need to support.
                        </xs:documentation>
                    </xs:annotation>
                    <xs:complexType>
                        <xs:choice>
                            <xs:element name="ambient">
                                <xs:annotation>
                                    <xs:documentation>
                                    The ambient element declares the parameters required to describe an ambient light source.
                                    An ambient light is one that lights everything evenly, regardless of location or orientation.
                                    </xs:documentation>
                                </xs:annotation>
                                <xs:complexType>
                                    <xs:sequence>
                                        <xs:element name="color" type="TargetableFloat3">
                                            <xs:annotation>
                                                <xs:documentation>
                                                The color element contains three floating point numbers specifying the color of the light.
                                                The color element must occur exactly once.
                                                </xs:documentation>
                                            </xs:annotation>
                                        </xs:element>
                                    </xs:sequence>
                                </xs:complexType>
                            </xs:element>
                            <xs:element name="directional">
                                <xs:annotation>
                                    <xs:documentation>
                                    The directional element declares the parameters required to describe a directional light source.
                                    A directional light is one that lights everything from the same direction, regardless of location.
                                    The light’s default direction vector in local coordinates is [0,0,-1], pointing down the -Z axis.
                                    The actual direction of the light is defined by the transform of the node where the light is
                                    instantiated.
                                    </xs:documentation>
                                </xs:annotation>
                                <xs:complexType>
                                    <xs:sequence>
                                        <xs:element name="color" type="TargetableFloat3">
                                            <xs:annotation>
                                                <xs:documentation>
                                                The color element contains three floating point numbers specifying the color of the light.
                                                The color element must occur exactly once.
                                                </xs:documentation>
                                            </xs:annotation>
                                        </xs:element>
                                    </xs:sequence>
                                </xs:complexType>
                            </xs:element>
                            <xs:element name="point">
                                <xs:annotation>
                                    <xs:documentation>
                                    The point element declares the parameters required to describe a point light source.  A point light
                                    source radiates light in all directions from a known location in space. The intensity of a point
                                    light source is attenuated as the distance to the light source increases. The position of the light
                                    is defined by the transform of the node in which it is instantiated.
                                    </xs:documentation>
                                </xs:annotation>
                                <xs:complexType>
                                    <xs:sequence>
                                        <xs:element name="color" type="TargetableFloat3">
                                            <xs:annotation>
                                                <xs:documentation>
                                                The color element contains three floating point numbers specifying the color of the light.
                                                The color element must occur exactly once.
                                                </xs:documentation>
                                            </xs:annotation>
                                        </xs:element>
                                        <xs:element name="constant_attenuation" type="TargetableFloat" default="1.0" minOccurs="0">
                                            <xs:annotation>
                                                <xs:documentation>
                                                The constant_attenuation is used to calculate the total attenuation of this light given a distance.
                                                The equation used is A = constant_attenuation + Dist*linear_attenuation + Dist^2*quadratic_attenuation.
                                                </xs:documentation>
                                            </xs:annotation>
                                        </xs:element>
                                        <xs:element name="linear_attenuation" type="TargetableFloat" default="0.0" minOccurs="0">
                                            <xs:annotation>
                                                <xs:documentation>
                                                The linear_attenuation is used to calculate the total attenuation of this light given a distance.
                                                The equation used is A = constant_attenuation + Dist*linear_attenuation + Dist^2*quadratic_attenuation.
                                                </xs:documentation>
                                            </xs:annotation>
                                        </xs:element>
                                        <xs:element name="quadratic_attenuation" type="TargetableFloat" default="0.0" minOccurs="0">
                                            <xs:annotation>
                                                <xs:documentation>
                                                The quadratic_attenuation is used to calculate the total attenuation of this light given a distance.
                                                The equation used is A = constant_attenuation + Dist*linear_attenuation + Dist^2*quadratic_attenuation.
                                                </xs:documentation>
                                            </xs:annotation>
                                        </xs:element>
                                    </xs:sequence>
                                </xs:complexType>
                            </xs:element>
                            <xs:element name="spot">
                                <xs:annotation>
                                    <xs:documentation>
                                    The spot element declares the parameters required to describe a spot light source.  A spot light
                                    source radiates light in one direction from a known location in space. The light radiates from
                                    the spot light source in a cone shape. The intensity of the light is attenuated as the radiation
                                    angle increases away from the direction of the light source. The intensity of a spot light source
                                    is also attenuated as the distance to the light source increases. The position of the light is
                                    defined by the transform of the node in which it is instantiated. The light’s default direction
                                    vector in local coordinates is [0,0,-1], pointing down the -Z axis. The actual direction of the
                                    light is defined by the transform of the node where the light is instantiated.
                                    </xs:documentation>
                                </xs:annotation>
                                <xs:complexType>
                                    <xs:sequence>
                                        <xs:element name="color" type="TargetableFloat3">
                                            <xs:annotation>
                                                <xs:documentation>
                                                The color element contains three floating point numbers specifying the color of the light.
                                                The color element must occur exactly once.
                                                </xs:documentation>
                                            </xs:annotation>
                                        </xs:element>
                                        <xs:element name="constant_attenuation" type="TargetableFloat" default="1.0" minOccurs="0">
                                            <xs:annotation>
                                                <xs:documentation>
                                                The constant_attenuation is used to calculate the total attenuation of this light given a distance.
                                                The equation used is A = constant_attenuation + Dist*linear_attenuation + Dist^2*quadratic_attenuation.
                                                </xs:documentation>
                                            </xs:annotation>
                                        </xs:element>
                                        <xs:element name="linear_attenuation" type="TargetableFloat" default="0.0" minOccurs="0">
                                            <xs:annotation>
                                                <xs:documentation>
                                                The linear_attenuation is used to calculate the total attenuation of this light given a distance.
                                                The equation used is A = constant_attenuation + Dist*linear_attenuation + Dist^2*quadratic_attenuation.
                                                </xs:documentation>
                                            </xs:annotation>
                                        </xs:element>
                                        <xs:element name="quadratic_attenuation" type="TargetableFloat" default="0.0" minOccurs="0">
                                            <xs:annotation>
                                                <xs:documentation>
                                                The quadratic_attenuation is used to calculate the total attenuation of this light given a distance.
                                                The equation used is A = constant_attenuation + Dist*linear_attenuation + Dist^2*quadratic_attenuation.
                                                </xs:documentation>
                                            </xs:annotation>
                                        </xs:element>
                                        <xs:element name="falloff_angle" type="TargetableFloat" default="180.0" minOccurs="0">
                                            <xs:annotation>
                                                <xs:documentation>
                                                The falloff_angle is used to specify the amount of attenuation based on the direction of the light.
                                                </xs:documentation>
                                            </xs:annotation>
                                        </xs:element>
                                        <xs:element name="falloff_exponent" type="TargetableFloat" default="0.0" minOccurs="0">
                                            <xs:annotation>
                                                <xs:documentation>
                                                The falloff_exponent is used to specify the amount of attenuation based on the direction of the light.
                                                </xs:documentation>
                                            </xs:annotation>
                                        </xs:element>
                                    </xs:sequence>
                                </xs:complexType>
                            </xs:element>
                        </xs:choice>
                    </xs:complexType>
                </xs:element>
                <xs:element ref="technique" minOccurs="0" maxOccurs="unbounded">
                    <xs:annotation>
                        <xs:documentation>
                        This element may contain any number of non-common profile techniques.
                        </xs:documentation>
                    </xs:annotation>
                </xs:element>
                <xs:element ref="extra" minOccurs="0" maxOccurs="unbounded">
                    <xs:annotation>
                        <xs:documentation>
                        The extra element may appear any number of times.
                        </xs:documentation>
                    </xs:annotation>
                </xs:element>
            </xs:sequence>
            <xs:attribute name="id" type="xs:ID">
                <xs:annotation>
                    <xs:documentation>
                    The id attribute is a text string containing the unique identifier of this element.
                    This value must be unique within the instance document. Optional attribute.
                    </xs:documentation>
                </xs:annotation>
            </xs:attribute>
            <xs:attribute name="name" type="xs:NCName">
                <xs:annotation>
                    <xs:documentation>
                    The name attribute is the text string name of this element. Optional attribute.
                    </xs:documentation>
                </xs:annotation>
            </xs:attribute>
        </xs:complexType>
    </xs:element>
    <xs:element name="material">
        <xs:annotation>
            <xs:documentation>
            Materials describe the visual appearance of a geometric object.
            </xs:documentation>
        </xs:annotation>
        <xs:complexType>
            <xs:sequence>
                <xs:element ref="asset" minOccurs="0">
                    <xs:annotation>
                        <xs:documentation>
                        The material element may contain an asset element.
                        </xs:documentation>
                    </xs:annotation>
                </xs:element>
                <xs:element ref="instance_effect">
                    <xs:annotation>
                        <xs:documentation>
                        The material must instance an effect.
                        </xs:documentation>
                    </xs:annotation>
                </xs:element>
                <xs:element ref="extra" minOccurs="0" maxOccurs="unbounded">
                    <xs:annotation>
                        <xs:documentation>
                        The extra element may appear any number of times.
                        </xs:documentation>
                    </xs:annotation>
                </xs:element>
            </xs:sequence>
            <xs:attribute name="id" type="xs:ID">
                <xs:annotation>
                    <xs:documentation>
                    The id attribute is a text string containing the unique identifier of this element. This value
                    must be unique within the instance document. Optional attribute.
                    </xs:documentation>
                </xs:annotation>
            </xs:attribute>
            <xs:attribute name="name" type="xs:NCName">
                <xs:annotation>
                    <xs:documentation>
                    The name attribute is the text string name of this element. Optional attribute.
                    </xs:documentation>
                </xs:annotation>
            </xs:attribute>
        </xs:complexType>
    </xs:element>
    <!-- Object Elements -->
    <xs:element name="camera">
        <xs:annotation>
            <xs:documentation>
            The camera element declares a view into the scene hierarchy or scene graph. The camera contains
            elements that describe the camera’s optics and imager.
            </xs:documentation>
        </xs:annotation>
        <xs:complexType>
            <xs:sequence>
                <xs:element ref="asset" minOccurs="0">
                    <xs:annotation>
                        <xs:documentation>
                        The camera element may contain an asset element.
                        </xs:documentation>
                    </xs:annotation>
                </xs:element>
                <xs:element name="optics">
                    <xs:annotation>
                        <xs:documentation>
                        Optics represents the apparatus on a camera that projects the image onto the image sensor.
                        </xs:documentation>
                    </xs:annotation>
                    <xs:complexType>
                        <xs:sequence>
                            <xs:element name="technique_common">
                                <xs:annotation>
                                    <xs:documentation>
                                    The technique_common element specifies the optics information for the common profile
                                    which all COLLADA implementations need to support.
                                    </xs:documentation>
                                </xs:annotation>
                                <xs:complexType>
                                    <xs:choice>
                                        <xs:element name="orthographic">
                                            <xs:annotation>
                                                <xs:documentation>
                                                The orthographic element describes the field of view of an orthographic camera.
                                                </xs:documentation>
                                            </xs:annotation>
                                            <xs:complexType>
                                                <xs:sequence>
                                                    <xs:choice>
                                                        <xs:sequence>
                                                            <xs:element name="xmag" type="TargetableFloat">
                                                                <xs:annotation>
                                                                    <xs:documentation>
                                                                    The xmag element contains a floating point number describing the horizontal
                                                                    magnification of the view.
                                                                    </xs:documentation>
                                                                </xs:annotation>
                                                            </xs:element>
                                                            <xs:choice minOccurs="0">
                                                                <xs:element name="ymag" type="TargetableFloat">
                                                                    <xs:annotation>
                                                                        <xs:documentation>
                                                                        The ymag element contains a floating point number describing the vertical
                                                                        magnification of the view.  It can also have a sid.
                                                                        </xs:documentation>
                                                                    </xs:annotation>
                                                                </xs:element>
                                                                <xs:element name="aspect_ratio" type="TargetableFloat">
                                                                    <xs:annotation>
                                                                        <xs:documentation>
                                                                        The aspect_ratio element contains a floating point number describing the aspect ratio of
                                                                        the field of view. If the aspect_ratio element is not present the aspect ratio is to be
                                                                        calculated from the xmag or ymag elements and the current viewport.
                                                                        </xs:documentation>
                                                                    </xs:annotation>
                                                                </xs:element>
                                                            </xs:choice>
                                                        </xs:sequence>
                                                        <xs:sequence>
                                                            <xs:element name="ymag" type="TargetableFloat"/>
                                                            <xs:element name="aspect_ratio" type="TargetableFloat" minOccurs="0"/>
                                                        </xs:sequence>
                                                    </xs:choice>
                                                    <xs:element name="znear" type="TargetableFloat">
                                                        <xs:annotation>
                                                            <xs:documentation>
                                                            The znear element contains a floating point number that describes the distance to the near
                                                            clipping plane. The znear element must occur exactly once.
                                                            </xs:documentation>
                                                        </xs:annotation>
                                                    </xs:element>
                                                    <xs:element name="zfar" type="TargetableFloat">
                                                        <xs:annotation>
                                                            <xs:documentation>
                                                            The zfar element contains a floating point number that describes the distance to the far
                                                            clipping plane. The zfar element must occur exactly once.
                                                            </xs:documentation>
                                                        </xs:annotation>
                                                    </xs:element>
                                                </xs:sequence>
                                            </xs:complexType>
                                        </xs:element>
                                        <xs:element name="perspective">
                                            <xs:annotation>
                                                <xs:documentation>
                                                The perspective element describes the optics of a perspective camera.
                                                </xs:documentation>
                                            </xs:annotation>
                                            <xs:complexType>
                                                <xs:sequence>
                                                    <xs:choice>
                                                        <xs:sequence>
                                                            <xs:element name="xfov" type="TargetableFloat">
                                                                <xs:annotation>
                                                                    <xs:documentation>
                                                                    The xfov element contains a floating point number describing the horizontal field of view in degrees.
                                                                    </xs:documentation>
                                                                </xs:annotation>
                                                            </xs:element>
                                                            <xs:choice minOccurs="0">
                                                                <xs:element name="yfov" type="TargetableFloat">
                                                                    <xs:annotation>
                                                                        <xs:documentation>
                                                                        The yfov element contains a floating point number describing the verticle field of view in degrees.
                                                                        </xs:documentation>
                                                                    </xs:annotation>
                                                                </xs:element>
                                                                <xs:element name="aspect_ratio" type="TargetableFloat">
                                                                    <xs:annotation>
                                                                        <xs:documentation>
                                                                        The aspect_ratio element contains a floating point number describing the aspect ratio of the field
                                                                        of view. If the aspect_ratio element is not present the aspect ratio is to be calculated from the
                                                                        xfov or yfov elements and the current viewport.
                                                                        </xs:documentation>
                                                                    </xs:annotation>
                                                                </xs:element>
                                                            </xs:choice>
                                                        </xs:sequence>
                                                        <xs:sequence>
                                                            <xs:element name="yfov" type="TargetableFloat"/>
                                                            <xs:element name="aspect_ratio" type="TargetableFloat" minOccurs="0"/>
                                                        </xs:sequence>
                                                    </xs:choice>
                                                    <xs:element name="znear" type="TargetableFloat">
                                                        <xs:annotation>
                                                            <xs:documentation>
                                                            The znear element contains a floating point number that describes the distance to the near
                                                            clipping plane. The znear element must occur exactly once.
                                                            </xs:documentation>
                                                        </xs:annotation>
                                                    </xs:element>
                                                    <xs:element name="zfar" type="TargetableFloat">
                                                        <xs:annotation>
                                                            <xs:documentation>
                                                            The zfar element contains a floating point number that describes the distance to the far
                                                            clipping plane. The zfar element must occur exactly once.
                                                            </xs:documentation>
                                                        </xs:annotation>
                                                    </xs:element>
                                                </xs:sequence>
                                            </xs:complexType>
                                        </xs:element>
                                    </xs:choice>
                                </xs:complexType>
                            </xs:element>
                            <xs:element ref="technique" minOccurs="0" maxOccurs="unbounded">
                                <xs:annotation>
                                    <xs:documentation>
                                    This element may contain any number of non-common profile techniques.
                                    </xs:documentation>
                                </xs:annotation>
                            </xs:element>
                            <xs:element ref="extra" minOccurs="0" maxOccurs="unbounded">
                                <xs:annotation>
                                    <xs:documentation>
                                    The extra element may appear any number of times.
                                    </xs:documentation>
                                </xs:annotation>
                            </xs:element>
                        </xs:sequence>
                    </xs:complexType>
                </xs:element>
                <xs:element name="imager" minOccurs="0">
                    <xs:annotation>
                        <xs:documentation>
                        Imagers represent the image sensor of a camera (for example film or CCD).
                        </xs:documentation>
                    </xs:annotation>
                    <xs:complexType>
                        <xs:sequence>
                            <xs:element ref="technique" maxOccurs="unbounded">
                                <xs:annotation>
                                    <xs:documentation>
                                    This element may contain any number of non-common profile techniques.
                                    There is no common technique for imager.
                                    </xs:documentation>
                                </xs:annotation>
                            </xs:element>
                            <xs:element ref="extra" minOccurs="0" maxOccurs="unbounded">
                                <xs:annotation>
                                    <xs:documentation>
                                    The extra element may appear any number of times.
                                    </xs:documentation>
                                </xs:annotation>
                            </xs:element>
                        </xs:sequence>
                    </xs:complexType>
                </xs:element>
                <xs:element ref="extra" minOccurs="0" maxOccurs="unbounded">
                    <xs:annotation>
                        <xs:documentation>
                        The extra element may appear any number of times.
                        </xs:documentation>
                    </xs:annotation>
                </xs:element>
            </xs:sequence>
            <xs:attribute name="id" type="xs:ID">
                <xs:annotation>
                    <xs:documentation>
                    The id attribute is a text string containing the unique identifier of this element. This value
                    must be unique within the instance document. Optional attribute.
                    </xs:documentation>
                </xs:annotation>
            </xs:attribute>
            <xs:attribute name="name" type="xs:NCName">
                <xs:annotation>
                    <xs:documentation>
                    The name attribute is the text string name of this element. Optional attribute.
                    </xs:documentation>
                </xs:annotation>
            </xs:attribute>
        </xs:complexType>
    </xs:element>
    <!-- Animation Elements -->
    <xs:element name="animation">
        <xs:annotation>
            <xs:documentation>
            The animation element categorizes the declaration of animation information. The animation
            hierarchy contains elements that describe the animation’s key-frame data and sampler functions,
            ordered in such a way to group together animations that should be executed together.
            </xs:documentation>
        </xs:annotation>
        <xs:complexType>
            <xs:sequence>
                <xs:element ref="asset" minOccurs="0">
                    <xs:annotation>
                        <xs:documentation>
                        The animation element may contain an asset element.
                        </xs:documentation>
                    </xs:annotation>
                </xs:element>
                <xs:choice>
                    <xs:sequence>
                        <xs:element ref="source" maxOccurs="unbounded">
                            <xs:annotation>
                                <xs:documentation>
                                The animation element may contain any number of source elements.
                                </xs:documentation>
                            </xs:annotation>
                        </xs:element>
                        <xs:choice>
                            <xs:sequence>
                                <xs:element ref="sampler" maxOccurs="unbounded">
                                    <xs:annotation>
                                        <xs:documentation>
                                        The animation element may contain any number of sampler elements.
                                        </xs:documentation>
                                    </xs:annotation>
                                </xs:element>
                                <xs:element ref="channel" maxOccurs="unbounded">
                                    <xs:annotation>
                                        <xs:documentation>
                                        The animation element may contain any number of channel elements.
                                        </xs:documentation>
                                    </xs:annotation>
                                </xs:element>
                                <xs:element ref="animation" minOccurs="0" maxOccurs="unbounded">
                                    <xs:annotation>
                                        <xs:documentation>
                                        The animation may be hierarchical and may contain any number of other animation elements.
                                        </xs:documentation>
                                    </xs:annotation>
                                </xs:element>
                            </xs:sequence>
                            <xs:element ref="animation" maxOccurs="unbounded"/>
                        </xs:choice>
                    </xs:sequence>
                    <xs:sequence>
                        <xs:element ref="sampler" maxOccurs="unbounded"/>
                        <xs:element ref="channel" maxOccurs="unbounded"/>
                        <xs:element ref="animation" minOccurs="0" maxOccurs="unbounded"/>
                    </xs:sequence>
                    <xs:element ref="animation" maxOccurs="unbounded"/>
                </xs:choice>
                <xs:element ref="extra" minOccurs="0" maxOccurs="unbounded">
                    <xs:annotation>
                        <xs:documentation>
                        The extra element may appear any number of times.
                        </xs:documentation>
                    </xs:annotation>
                </xs:element>
            </xs:sequence>
            <xs:attribute name="id" type="xs:ID">
                <xs:annotation>
                    <xs:documentation>
                    The id attribute is a text string containing the unique identifier of this element. This value
                    must be unique within the instance document. Optional attribute.
                    </xs:documentation>
                </xs:annotation>
            </xs:attribute>
            <xs:attribute name="name" type="xs:NCName">
                <xs:annotation>
                    <xs:documentation>
                    The name attribute is the text string name of this element. Optional attribute.
                    </xs:documentation>
                </xs:annotation>
            </xs:attribute>
        </xs:complexType>
    </xs:element>
    <xs:element name="animation_clip">
        <xs:annotation>
            <xs:documentation>
            The animation_clip element defines a section of the animation curves to be used together as
            an animation clip.
            </xs:documentation>
        </xs:annotation>
        <xs:complexType>
            <xs:sequence>
                <xs:element ref="asset" minOccurs="0">
                    <xs:annotation>
                        <xs:documentation>
                        The animation_clip element may contain an asset element.
                        </xs:documentation>
                    </xs:annotation>
                </xs:element>
                <xs:element name="instance_animation" type="InstanceWithExtra" maxOccurs="unbounded">
                    <xs:annotation>
                        <xs:documentation>
                        The animation_clip must instance at least one animation element.
                        </xs:documentation>
                    </xs:annotation>
                </xs:element>
                <xs:element ref="extra" minOccurs="0" maxOccurs="unbounded">
                    <xs:annotation>
                        <xs:documentation>
                        The extra element may appear any number of times.
                        </xs:documentation>
                    </xs:annotation>
                </xs:element>
            </xs:sequence>
            <xs:attribute name="id" type="xs:ID">
                <xs:annotation>
                    <xs:documentation>
                    The id attribute is a text string containing the unique identifier of this element.
                    This value must be unique within the instance document. Optional attribute.
                    </xs:documentation>
                </xs:annotation>
            </xs:attribute>
            <xs:attribute name="name" type="xs:NCName">
                <xs:annotation>
                    <xs:documentation>
                    The name attribute is the text string name of this element. Optional attribute.
                    </xs:documentation>
                </xs:annotation>
            </xs:attribute>
            <xs:attribute name="start" type="xs:double" default="0.0">
                <xs:annotation>
                    <xs:documentation>
                    The start attribute is the time in seconds of the beginning of the clip.  This time is
                    the same as that used in the key-frame data and is used to determine which set of
                    key-frames will be included in the clip.  The start time does not specify when the clip
                    will be played.  If the time falls between two keyframes of a referenced animation, an
                    interpolated value should be used.  The default value is 0.0.  Optional attribute.
                    </xs:documentation>
                </xs:annotation>
            </xs:attribute>
            <xs:attribute name="end" type="xs:double">
                <xs:annotation>
                    <xs:documentation>
                    The end attribute is the time in seconds of the end of the clip.  This is used in the
                    same way as the start time.  If end is not specified, the value is taken to be the end
                    time of the longest animation.  Optional attribute.
                    </xs:documentation>
                </xs:annotation>
            </xs:attribute>
        </xs:complexType>
    </xs:element>
    <xs:element name="channel">
        <xs:annotation>
            <xs:documentation>
            The channel element declares an output channel of an animation.
            </xs:documentation>
        </xs:annotation>
        <xs:complexType>
            <xs:attribute name="source" type="URIFragmentType" use="required">
                <xs:annotation>
                    <xs:documentation>
                    The source attribute indicates the location of the sampler using a URL expression.
                    The sampler must be declared within the same document. Required attribute.
                    </xs:documentation>
                </xs:annotation>
            </xs:attribute>
            <xs:attribute name="target" type="xs:token" use="required">
                <xs:annotation>
                    <xs:documentation>
                    The target attribute indicates the location of the element bound to the output of the sampler.
                    This text string is a path-name following a simple syntax described in Address Syntax.
                    Required attribute.
                    </xs:documentation>
                </xs:annotation>
            </xs:attribute>
        </xs:complexType>
    </xs:element>
    <xs:element name="sampler">
        <xs:annotation>
            <xs:documentation>
            The sampler element declares an N-dimensional function used for animation. Animation function curves
            are represented by 1-D sampler elements in COLLADA. The sampler defines sampling points and how to
            interpolate between them.
            </xs:documentation>
        </xs:annotation>
        <xs:complexType>
            <xs:sequence>
                <xs:element name="input" type="InputLocal" maxOccurs="unbounded">
                    <xs:annotation>
                        <xs:documentation>
                        The input element must occur at least one time. These inputs are local inputs.
                        </xs:documentation>
                    </xs:annotation>
                </xs:element>
            </xs:sequence>
            <xs:attribute name="id" type="xs:ID">
                <xs:annotation>
                    <xs:documentation>
                    The id attribute is a text string containing the unique identifier of this element. This value
                    must be unique within the instance document. Optional attribute.
                    </xs:documentation>
                </xs:annotation>
            </xs:attribute>
        </xs:complexType>
    </xs:element>
    <!-- Controller Elements -->
    <xs:element name="controller">
        <xs:annotation>
            <xs:documentation>
            The controller element categorizes the declaration of generic control information.
            A controller is a device or mechanism that manages and directs the operations of another object.
            </xs:documentation>
        </xs:annotation>
        <xs:complexType>
            <xs:sequence>
                <xs:element ref="asset" minOccurs="0">
                    <xs:annotation>
                        <xs:documentation>
                        The controller element may contain an asset element.
                        </xs:documentation>
                    </xs:annotation>
                </xs:element>
                <xs:choice>
                    <xs:element ref="skin">
                        <xs:annotation>
                            <xs:documentation>
                            The controller element may contain either a skin element or a morph element.
                            </xs:documentation>
                        </xs:annotation>
                    </xs:element>
                    <xs:element ref="morph">
                        <xs:annotation>
                            <xs:documentation>
                            The controller element may contain either a skin element or a morph element.
                            </xs:documentation>
                        </xs:annotation>
                    </xs:element>
                </xs:choice>
                <xs:element ref="extra" minOccurs="0" maxOccurs="unbounded">
                    <xs:annotation>
                        <xs:documentation>
                        The extra element may appear any number of times.
                        </xs:documentation>
                    </xs:annotation>
                </xs:element>
            </xs:sequence>
            <xs:attribute name="id" type="xs:ID">
                <xs:annotation>
                    <xs:documentation>
                    The id attribute is a text string containing the unique identifier of this element. This value
                    must be unique within the instance document. Optional attribute.
                    </xs:documentation>
                </xs:annotation>
            </xs:attribute>
            <xs:attribute name="name" type="xs:NCName">
                <xs:annotation>
                    <xs:documentation>
                    The name attribute is the text string name of this element. Optional attribute.
                    </xs:documentation>
                </xs:annotation>
            </xs:attribute>
        </xs:complexType>
    </xs:element>
    <xs:element name="skin">
        <xs:annotation>
            <xs:documentation>
            The skin element contains vertex and primitive information sufficient to describe blend-weight skinning.
            </xs:documentation>
        </xs:annotation>
        <xs:complexType>
            <xs:sequence>
                <xs:element name="bind_shape_matrix" type="float4x4" minOccurs="0">
                    <xs:annotation>
                        <xs:documentation>
                        This provides extra information about the position and orientation of the base mesh before binding.
                        If bind_shape_matrix is not specified then an identity matrix may be used as the bind_shape_matrix.
                        The bind_shape_matrix element may occur zero or one times.
                        </xs:documentation>
                    </xs:annotation>
                </xs:element>
                <xs:element ref="source" minOccurs="3" maxOccurs="unbounded">
                    <xs:annotation>
                        <xs:documentation>
                        The skin element must contain at least three source elements.
                        </xs:documentation>
                    </xs:annotation>
                </xs:element>
                <xs:element name="joints">
                    <xs:annotation>
                        <xs:documentation>
                        The joints element associates joint, or skeleton, nodes with attribute data.
                        In COLLADA, this is specified by the inverse bind matrix of each joint (influence) in the skeleton.
                        </xs:documentation>
                    </xs:annotation>
                    <xs:complexType>
                        <xs:sequence>
                            <xs:element name="input" type="InputLocal" minOccurs="2" maxOccurs="unbounded">
                                <xs:annotation>
                                    <xs:documentation>
                                    The input element must occur at least twice. These inputs are local inputs.
                                    </xs:documentation>
                                </xs:annotation>
                            </xs:element>
                            <xs:element ref="extra" minOccurs="0" maxOccurs="unbounded">
                                <xs:annotation>
                                    <xs:documentation>
                                    The extra element may appear any number of times.
                                    </xs:documentation>
                                </xs:annotation>
                            </xs:element>
                        </xs:sequence>
                    </xs:complexType>
                </xs:element>
                <xs:element name="vertex_weights">
                    <xs:annotation>
                        <xs:documentation>
                        The vertex_weights element associates a set of joint-weight pairs with each vertex in the base mesh.
                        </xs:documentation>
                    </xs:annotation>
                    <xs:complexType>
                        <xs:sequence>
                            <xs:element name="input" type="InputLocalOffset" minOccurs="2" maxOccurs="unbounded">
                                <xs:annotation>
                                    <xs:documentation>
                                    The input element must occur at least twice.
                                    </xs:documentation>
                                </xs:annotation>
                            </xs:element>
                            <xs:element name="vcount" type="ListOfUInts" minOccurs="0">
                                <xs:annotation>
                                    <xs:documentation>
                                    The vcount element contains a list of integers describing the number of influences for each vertex.
                                    The vcount element may occur once.
                                    </xs:documentation>
                                </xs:annotation>
                            </xs:element>
                            <xs:element name="v" type="ListOfInts" minOccurs="0">
                                <xs:annotation>
                                    <xs:documentation>
                                    The v element describes which bones and attributes are associated with each vertex.  An index
                                    of –1 into the array of joints refers to the bind shape.  Weights should be normalized before use.
                                    The v element must occur zero or one times.
                                    </xs:documentation>
                                </xs:annotation>
                            </xs:element>
                            <xs:element ref="extra" minOccurs="0" maxOccurs="unbounded">
                                <xs:annotation>
                                    <xs:documentation>
                                    The extra element may appear any number of times.
                                    </xs:documentation>
                                </xs:annotation>
                            </xs:element>
                        </xs:sequence>
                        <xs:attribute name="count" type="uint" use="required">
                            <xs:annotation>
                                <xs:documentation>
                                The count attribute describes the number of vertices in the base mesh. Required element.
                                </xs:documentation>
                            </xs:annotation>
                        </xs:attribute>
                    </xs:complexType>
                </xs:element>
                <xs:element ref="extra" minOccurs="0" maxOccurs="unbounded">
                    <xs:annotation>
                        <xs:documentation>
                        The extra element may appear any number of times.
                        </xs:documentation>
                    </xs:annotation>
                </xs:element>
            </xs:sequence>
            <xs:attribute name="source" type="xs:anyURI" use="required">
                <xs:annotation>
                    <xs:documentation>
                    The source attribute contains a URI reference to the base mesh, (a static mesh or a morphed mesh).
                    This also provides the bind-shape of the skinned mesh.  Required attribute.
                    </xs:documentation>
                </xs:annotation>
            </xs:attribute>
        </xs:complexType>
    </xs:element>
    <xs:element name="morph">
        <xs:annotation>
            <xs:documentation>
            The morph element describes the data required to blend between sets of static meshes. Each
            possible mesh that can be blended (a morph target) must be specified.
            </xs:documentation>
        </xs:annotation>
        <xs:complexType>
            <xs:sequence>
                <xs:element ref="source" minOccurs="2" maxOccurs="unbounded">
                    <xs:annotation>
                        <xs:documentation>
                        The morph element must contain at least two source elements.
                        </xs:documentation>
                    </xs:annotation>
                </xs:element>
                <xs:element name="targets">
                    <xs:annotation>
                        <xs:documentation>
                        The targets element declares the morph targets, their weights and any user defined attributes
                        associated with them.
                        </xs:documentation>
                    </xs:annotation>
                    <xs:complexType>
                        <xs:sequence>
                            <xs:element name="input" type="InputLocal" minOccurs="2" maxOccurs="unbounded">
                                <xs:annotation>
                                    <xs:documentation>
                                    The input element must occur at least twice. These inputs are local inputs.
                                    </xs:documentation>
                                </xs:annotation>
                            </xs:element>
                            <xs:element ref="extra" minOccurs="0" maxOccurs="unbounded">
                                <xs:annotation>
                                    <xs:documentation>
                                    The extra element may appear any number of times.
                                    </xs:documentation>
                                </xs:annotation>
                            </xs:element>
                        </xs:sequence>
                    </xs:complexType>
                </xs:element>
                <xs:element ref="extra" minOccurs="0" maxOccurs="unbounded">
                    <xs:annotation>
                        <xs:documentation>
                        The extra element may appear any number of times.
                        </xs:documentation>
                    </xs:annotation>
                </xs:element>
            </xs:sequence>
            <xs:attribute name="method" type="MorphMethodType" default="NORMALIZED">
                <xs:annotation>
                    <xs:documentation>
                    The method attribute specifies the which blending technique to use. The accepted values are
                    NORMALIZED, and RELATIVE. The default value if not specified is NORMALIZED.  Optional attribute.
                    </xs:documentation>
                </xs:annotation>
            </xs:attribute>
            <xs:attribute name="source" type="xs:anyURI" use="required">
                <xs:annotation>
                    <xs:documentation>
                    The source attribute indicates the base mesh. Required attribute.
                    </xs:documentation>
                </xs:annotation>
            </xs:attribute>
        </xs:complexType>
    </xs:element>
    <!-- Meta Elements -->
    <xs:element name="asset">
        <xs:annotation>
            <xs:documentation>
            The asset element defines asset management information regarding its parent element.
            </xs:documentation>
        </xs:annotation>
        <xs:complexType>
            <xs:sequence>
                <xs:element name="contributor" minOccurs="0" maxOccurs="unbounded">
                    <xs:annotation>
                        <xs:documentation>
                        The contributor element defines authoring information for asset management
                        </xs:documentation>
                    </xs:annotation>
                    <xs:complexType>
                        <xs:sequence>
                            <xs:element name="author" type="xs:string" minOccurs="0">
                                <xs:annotation>
                                    <xs:documentation>
                                    The author element contains a string with the author's name.
                                    There may be only one author element.
                                    </xs:documentation>
                                </xs:annotation>
                            </xs:element>
                            <xs:element name="authoring_tool" type="xs:string" minOccurs="0">
                                <xs:annotation>
                                    <xs:documentation>
                                    The authoring_tool element contains a string with the authoring tool's name.
                                    There may be only one authoring_tool element.
                                    </xs:documentation>
                                </xs:annotation>
                            </xs:element>
                            <xs:element name="comments" type="xs:string" minOccurs="0">
                                <xs:annotation>
                                    <xs:documentation>
                                    The comments element contains a string with comments from this contributor.
                                    There may be only one comments element.
                                    </xs:documentation>
                                </xs:annotation>
                            </xs:element>
                            <xs:element name="copyright" type="xs:string" minOccurs="0">
                                <xs:annotation>
                                    <xs:documentation>
                                    The copyright element contains a string with copyright information.
                                    There may be only one copyright element.
                                    </xs:documentation>
                                </xs:annotation>
                            </xs:element>
                            <xs:element name="source_data" type="xs:anyURI" minOccurs="0">
                                <xs:annotation>
                                    <xs:documentation>
                                    The source_data element contains a URI reference to the source data used for this asset.
                                    There may be only one source_data element.
                                    </xs:documentation>
                                </xs:annotation>
                            </xs:element>
                        </xs:sequence>
                    </xs:complexType>
                </xs:element>
                <xs:element name="created" type="xs:dateTime">
                    <xs:annotation>
                        <xs:documentation>
                        The created element contains the date and time that the parent element was created and is
                        represented in an ISO 8601 format.  The created element may appear zero or one time.
                        </xs:documentation>
                    </xs:annotation>
                </xs:element>
                <xs:element name="keywords" type="xs:string" minOccurs="0">
                    <xs:annotation>
                        <xs:documentation>
                        The keywords element contains a list of words used as search criteria for the parent element.
                        The keywords element may appear zero or more times.
                        </xs:documentation>
                    </xs:annotation>
                </xs:element>
                <xs:element name="modified" type="xs:dateTime">
                    <xs:annotation>
                        <xs:documentation>
                        The modified element contains the date and time that the parent element was last modified and
                        represented in an ISO 8601 format. The modified element may appear zero or one time.
                        </xs:documentation>
                    </xs:annotation>
                </xs:element>
                <xs:element name="revision" type="xs:string" minOccurs="0">
                    <xs:annotation>
                        <xs:documentation>
                        The revision element contains the revision information for the parent element. The revision
                        element may appear zero or one time.
                        </xs:documentation>
                    </xs:annotation>
                </xs:element>
                <xs:element name="subject" type="xs:string" minOccurs="0">
                    <xs:annotation>
                        <xs:documentation>
                        The subject element contains a description of the topical subject of the parent element. The
                        subject element may appear zero or one time.
                        </xs:documentation>
                    </xs:annotation>
                </xs:element>
                <xs:element name="title" type="xs:string" minOccurs="0">
                    <xs:annotation>
                        <xs:documentation>
                        The title element contains the title information for the parent element. The title element may
                        appear zero or one time.
                        </xs:documentation>
                    </xs:annotation>
                </xs:element>
                <xs:element name="unit" minOccurs="0">
                    <xs:annotation>
                        <xs:documentation>
                        The unit element contains descriptive information about unit of measure. It has attributes for
                        the name of the unit and the measurement with respect to the meter. The unit element may appear
                        zero or one time.
                        </xs:documentation>
                    </xs:annotation>
                    <xs:complexType>
                        <xs:attribute name="meter" type="float" default="1.0">
                            <xs:annotation>
                                <xs:documentation>
                                The meter attribute specifies the measurement with respect to the meter. The default
                                value for the meter attribute is “1.0”.
                                </xs:documentation>
                            </xs:annotation>
                        </xs:attribute>
                        <xs:attribute name="name" type="xs:NMTOKEN" default="meter">
                            <xs:annotation>
                                <xs:documentation>
                                The name attribute specifies the name of the unit. The default value for the name
                                attribute is “meter”.
                                </xs:documentation>
                            </xs:annotation>
                        </xs:attribute>
                    </xs:complexType>
                </xs:element>
                <xs:element name="up_axis" type="UpAxisType" default="Y_UP" minOccurs="0">
                    <xs:annotation>
                        <xs:documentation>
                        The up_axis element contains descriptive information about coordinate system of the geometric
                        data. All coordinates are right-handed by definition. This element specifies which axis is
                        considered up. The default is the Y-axis. The up_axis element may appear zero or one time.
                        </xs:documentation>
                    </xs:annotation>
                </xs:element>
            </xs:sequence>
        </xs:complexType>
    </xs:element>
    <xs:element name="extra">
        <xs:annotation>
            <xs:documentation>
            The extra element declares additional information regarding its parent element.
            </xs:documentation>
        </xs:annotation>
        <xs:complexType>
            <xs:sequence>
                <xs:element ref="asset" minOccurs="0">
                    <xs:annotation>
                        <xs:documentation>
                        The extra element may contain an asset element.
                        </xs:documentation>
                    </xs:annotation>
                </xs:element>
                <xs:element ref="technique" maxOccurs="unbounded">
                    <xs:annotation>
                        <xs:documentation>
                        This element must contain at least one non-common profile technique.
                        </xs:documentation>
                    </xs:annotation>
                </xs:element>
            </xs:sequence>
            <xs:attribute name="id" type="xs:ID">
                <xs:annotation>
                    <xs:documentation>
                    The id attribute is a text string containing the unique identifier of this element. This value
                    must be unique within the instance document. Optional attribute.
                    </xs:documentation>
                </xs:annotation>
            </xs:attribute>
            <xs:attribute name="name" type="xs:NCName">
                <xs:annotation>
                    <xs:documentation>
                    The name attribute is the text string name of this element. Optional attribute.
                    </xs:documentation>
                </xs:annotation>
            </xs:attribute>
            <xs:attribute name="type" type="xs:NMTOKEN">
                <xs:annotation>
                    <xs:documentation>
                    The type attribute indicates the type of the value data. This text string must be understood by
                    the application. Optional attribute.
                    </xs:documentation>
                </xs:annotation>
            </xs:attribute>
        </xs:complexType>
    </xs:element>
    <xs:element name="technique">
        <xs:annotation>
            <xs:appinfo>enable-xmlns</xs:appinfo>
            <xs:documentation>
            The technique element declares the information used to process some portion of the content. Each
            technique conforms to an associated profile. Techniques generally act as a “switch”. If more than
            one is present for a particular portion of content, on import, one or the other is picked, but
            usually not both. Selection should be based on which profile the importing application can support.
            Techniques contain application data and programs, making them assets that can be managed as a unit.
            </xs:documentation>
        </xs:annotation>
        <xs:complexType>
            <xs:sequence>
                <xs:any namespace="##any" processContents="lax" minOccurs="0" maxOccurs="unbounded"/>
            </xs:sequence>
            <xs:attribute name="profile" type="xs:NMTOKEN" use="required">
                <xs:annotation>
                    <xs:documentation>
                    The profile attribute indicates the type of profile. This is a vendor defined character
                    string that indicates the platform or capability target for the technique. Required attribute.
                    </xs:documentation>
                </xs:annotation>
            </xs:attribute>
        </xs:complexType>
    </xs:element>
    <!-- Hierarchical Elements -->
    <xs:element name="node">
        <xs:annotation>
            <xs:documentation>
            Nodes embody the hierarchical relationship of elements in the scene.
            </xs:documentation>
        </xs:annotation>
        <xs:complexType>
            <xs:sequence>
                <xs:element ref="asset" minOccurs="0">
                    <xs:annotation>
                        <xs:documentation>
                        The node element may contain an asset element.
                        </xs:documentation>
                    </xs:annotation>
                </xs:element>
                <xs:choice minOccurs="0" maxOccurs="unbounded">
                    <xs:element ref="lookat">
                        <xs:annotation>
                            <xs:documentation>
                            The node element may contain any number of lookat elements.
                            </xs:documentation>
                        </xs:annotation>
                    </xs:element>
                    <xs:element ref="matrix">
                        <xs:annotation>
                            <xs:documentation>
                            The node element may contain any number of matrix elements.
                            </xs:documentation>
                        </xs:annotation>
                    </xs:element>
                    <xs:element ref="rotate">
                        <xs:annotation>
                            <xs:documentation>
                            The node element may contain any number of rotate elements.
                            </xs:documentation>
                        </xs:annotation>
                    </xs:element>
                    <xs:element ref="scale">
                        <xs:annotation>
                            <xs:documentation>
                            The node element may contain any number of scale elements.
                            </xs:documentation>
                        </xs:annotation>
                    </xs:element>
                    <xs:element ref="skew">
                        <xs:annotation>
                            <xs:documentation>
                            The node element may contain any number of skew elements.
                            </xs:documentation>
                        </xs:annotation>
                    </xs:element>
                    <xs:element ref="translate">
                        <xs:annotation>
                            <xs:documentation>
                            The node element may contain any number of translate elements.
                            </xs:documentation>
                        </xs:annotation>
                    </xs:element>
                </xs:choice>
                <xs:element ref="instance_camera" minOccurs="0" maxOccurs="unbounded">
                    <xs:annotation>
                        <xs:documentation>
                        The node element may instance any number of camera objects.
                        </xs:documentation>
                    </xs:annotation>
                </xs:element>
                <xs:element ref="instance_controller" minOccurs="0" maxOccurs="unbounded">
                    <xs:annotation>
                        <xs:documentation>
                        The node element may instance any number of controller objects.
                        </xs:documentation>
                    </xs:annotation>
                </xs:element>
                <xs:element ref="instance_geometry" minOccurs="0" maxOccurs="unbounded">
                    <xs:annotation>
                        <xs:documentation>
                        The node element may instance any number of geometry objects.
                        </xs:documentation>
                    </xs:annotation>
                </xs:element>
                <xs:element ref="instance_light" minOccurs="0" maxOccurs="unbounded">
                    <xs:annotation>
                        <xs:documentation>
                        The node element may instance any number of light objects.
                        </xs:documentation>
                    </xs:annotation>
                </xs:element>
                <xs:element ref="instance_node" minOccurs="0" maxOccurs="unbounded">
                    <xs:annotation>
                        <xs:documentation>
                        The node element may instance any number of node elements or hierarchies objects.
                        </xs:documentation>
                    </xs:annotation>
                </xs:element>
                <xs:element ref="node" minOccurs="0" maxOccurs="unbounded">
                    <xs:annotation>
                        <xs:documentation>
                        The node element may be hierarchical and be the parent of any number of other node elements.
                        </xs:documentation>
                    </xs:annotation>
                </xs:element>
                <xs:element ref="extra" minOccurs="0" maxOccurs="unbounded">
                    <xs:annotation>
                        <xs:documentation>
                        The extra element may appear any number of times.
                        </xs:documentation>
                    </xs:annotation>
                </xs:element>
            </xs:sequence>
            <xs:attribute name="id" type="xs:ID">
                <xs:annotation>
                    <xs:documentation>
                    The id attribute is a text string containing the unique identifier of this element.
                    This value must be unique within the instance document. Optional attribute.
                    </xs:documentation>
                </xs:annotation>
            </xs:attribute>
            <xs:attribute name="name" type="xs:NCName">
                <xs:annotation>
                    <xs:documentation>
                    The name attribute is the text string name of this element. Optional attribute.
                    </xs:documentation>
                </xs:annotation>
            </xs:attribute>
            <xs:attribute name="sid" type="xs:NCName">
                <xs:annotation>
                    <xs:documentation>
                    The sid attribute is a text string value containing the sub-identifier of this element.
                    This value must be unique within the scope of the parent element. Optional attribute.
                    </xs:documentation>
                </xs:annotation>
            </xs:attribute>
            <xs:attribute name="type" type="NodeType" default="NODE">
                <xs:annotation>
                    <xs:documentation>
                    The type attribute indicates the type of the node element. The default value is “NODE”.
                    Optional attribute.
                    </xs:documentation>
                </xs:annotation>
            </xs:attribute>
            <xs:attribute name="layer" type="ListOfNames">
                <xs:annotation>
                    <xs:documentation>
                    The layer attribute indicates the names of the layers to which this node belongs.  For example,
                    a value of “foreground glowing” indicates that this node belongs to both the ‘foreground’ layer
                    and the ‘glowing’ layer.  The default value is empty, indicating that the node doesn’t belong to
                    any layer.  Optional attribute.
                    </xs:documentation>
                </xs:annotation>
            </xs:attribute>
        </xs:complexType>
    </xs:element>
    <xs:element name="visual_scene">
        <xs:annotation>
            <xs:documentation>
            The visual_scene element declares the base of the visual_scene hierarchy or scene graph. The
            scene contains elements that comprise much of the visual and transformational information
            content as created by the authoring tools.
            </xs:documentation>
        </xs:annotation>
        <xs:complexType>
            <xs:sequence>
                <xs:element ref="asset" minOccurs="0">
                    <xs:annotation>
                        <xs:documentation>
                        The visual_scene element may contain an asset element.
                        </xs:documentation>
                    </xs:annotation>
                </xs:element>
                <xs:element ref="node" maxOccurs="unbounded">
                    <xs:annotation>
                        <xs:documentation>
                        The visual_scene element must have at least one node element.
                        </xs:documentation>
                    </xs:annotation>
                </xs:element>
                <xs:element name="evaluate_scene" minOccurs="0" maxOccurs="unbounded">
                    <xs:annotation>
                        <xs:documentation>
                        The evaluate_scene element declares information specifying a specific way to evaluate this
                        visual_scene. There may be any number of evaluate_scene elements.
                        </xs:documentation>
                    </xs:annotation>
                    <xs:complexType>
                        <xs:sequence>
                            <xs:element name="render" maxOccurs="unbounded">
                                <xs:annotation>
                                    <xs:documentation>
                                    The render element describes one effect pass to evaluate the scene.
                                    There must be at least one render element.
                                    </xs:documentation>
                                </xs:annotation>
                                <xs:complexType>
                                    <xs:sequence>
                                        <xs:element name="layer" type="xs:NCName" minOccurs="0" maxOccurs="unbounded">
                                            <xs:annotation>
                                                <xs:documentation>
                                                The layer element specifies which layer to render in this compositing step
                                                while evaluating the scene. You may specify any number of layers.
                                                </xs:documentation>
                                            </xs:annotation>
                                        </xs:element>
                                        <xs:element ref="instance_effect" minOccurs="0">
                                            <xs:annotation>
                                                <xs:documentation>
                                                The instance_effect element specifies which effect to render in this compositing step
                                                while evaluating the scene.
                                                </xs:documentation>
                                            </xs:annotation>
                                        </xs:element>
                                    </xs:sequence>
                                    <xs:attribute name="camera_node" type="xs:anyURI" use="required">
                                        <xs:annotation>
                                            <xs:documentation>
                                            The camera_node attribute refers to a node that contains a camera describing the viewpoint to
                                            render this compositing step from.
                                            </xs:documentation>
                                        </xs:annotation>
                                    </xs:attribute>
                                </xs:complexType>
                            </xs:element>
                        </xs:sequence>
                        <xs:attribute name="name" type="xs:NCName">
                            <xs:annotation>
                                <xs:documentation>
                                The name attribute is the text string name of this element. Optional attribute.
                                </xs:documentation>
                            </xs:annotation>
                        </xs:attribute>
                    </xs:complexType>
                </xs:element>
                <xs:element ref="extra" minOccurs="0" maxOccurs="unbounded">
                    <xs:annotation>
                        <xs:documentation>
                        The extra element may appear any number of times.
                        </xs:documentation>
                    </xs:annotation>
                </xs:element>
            </xs:sequence>
            <xs:attribute name="id" type="xs:ID" use="optional">
                <xs:annotation>
                    <xs:documentation>
                    The id attribute is a text string containing the unique identifier of this element. This
                    value must be unique within the instance document. Optional attribute.
                    </xs:documentation>
                </xs:annotation>
            </xs:attribute>
            <xs:attribute name="name" type="xs:NCName">
                <xs:annotation>
                    <xs:documentation>
                    The name attribute is the text string name of this element. Optional attribute.
                    </xs:documentation>
                </xs:annotation>
            </xs:attribute>
        </xs:complexType>
    </xs:element>
    <!-- Instance Elements -->
    <xs:element name="bind_material">
        <xs:annotation>
            <xs:documentation>
            Bind a specific material to a piece of geometry, binding varying and uniform parameters at the
            same time.
            </xs:documentation>
        </xs:annotation>
        <xs:complexType>
            <xs:sequence>
                <xs:element ref="param" minOccurs="0" maxOccurs="unbounded">
                    <xs:annotation>
                        <xs:documentation>
                        The bind_material element may contain any number of param elements.
                        </xs:documentation>
                    </xs:annotation>
                </xs:element>
                <xs:element name="technique_common">
                    <xs:annotation>
                        <xs:documentation>
                        The technique_common element specifies the bind_material information for the common
                        profile which all COLLADA implementations need to support.
                        </xs:documentation>
                    </xs:annotation>
                    <xs:complexType>
                        <xs:sequence>
                            <xs:element ref="instance_material" maxOccurs="unbounded">
                                <xs:annotation>
                                    <xs:documentation>
                                    The instance_material element specifies the information needed to bind a geometry
                                    to a material. This element must appear at least once.
                                    </xs:documentation>
                                </xs:annotation>
                            </xs:element>
                        </xs:sequence>
                    </xs:complexType>
                </xs:element>
                <xs:element ref="technique" minOccurs="0" maxOccurs="unbounded">
                    <xs:annotation>
                        <xs:documentation>
                        This element may contain any number of non-common profile techniques.
                        </xs:documentation>
                    </xs:annotation>
                </xs:element>
                <xs:element ref="extra" minOccurs="0" maxOccurs="unbounded">
                    <xs:annotation>
                        <xs:documentation>
                        The extra element may appear any number of times.
                        </xs:documentation>
                    </xs:annotation>
                </xs:element>
            </xs:sequence>
        </xs:complexType>
    </xs:element>
    <xs:element name="instance_camera" type="InstanceWithExtra">
        <xs:annotation>
            <xs:documentation>
            The instance_camera element declares the instantiation of a COLLADA camera resource.
            </xs:documentation>
        </xs:annotation>
    </xs:element>
    <xs:element name="instance_controller">
        <xs:annotation>
            <xs:documentation>
            The instance_controller element declares the instantiation of a COLLADA controller resource.
            </xs:documentation>
        </xs:annotation>
        <xs:complexType>
            <xs:sequence>
                <xs:element name="skeleton" type="xs:anyURI" minOccurs="0" maxOccurs="unbounded">
                    <xs:annotation>
                        <xs:documentation>
                        The skeleton element is used to indicate where a skin controller is to start to search for
                        the joint nodes it needs.  This element is meaningless for morph controllers.
                        </xs:documentation>
                    </xs:annotation>
                </xs:element>
                <xs:element ref="bind_material" minOccurs="0">
                    <xs:annotation>
                        <xs:documentation>
                        Bind a specific material to a piece of geometry, binding varying and uniform parameters at the
                        same time.
                        </xs:documentation>
                    </xs:annotation>
                </xs:element>
                <xs:element ref="extra" minOccurs="0" maxOccurs="unbounded">
                    <xs:annotation>
                        <xs:documentation>
                        The extra element may appear any number of times.
                        </xs:documentation>
                    </xs:annotation>
                </xs:element>
            </xs:sequence>
            <xs:attribute name="url" type="xs:anyURI" use="required">
                <xs:annotation>
                    <xs:documentation>
                    The url attribute refers to resource. This may refer to a local resource using a relative
                    URL fragment identifier that begins with the “#” character. The url attribute may refer to an
                    external resource using an absolute or relative URL.
                    </xs:documentation>
                </xs:annotation>
            </xs:attribute>
            <xs:attribute name="sid" type="xs:NCName">
                <xs:annotation>
                    <xs:documentation>
                    The sid attribute is a text string value containing the sub-identifier of this element. This
                    value must be unique within the scope of the parent element. Optional attribute.
                    </xs:documentation>
                </xs:annotation>
            </xs:attribute>
            <xs:attribute name="name" type="xs:NCName">
                <xs:annotation>
                    <xs:documentation>
                    The name attribute is the text string name of this element. Optional attribute.
                    </xs:documentation>
                </xs:annotation>
            </xs:attribute>
        </xs:complexType>
    </xs:element>
    <xs:element name="instance_effect">
        <xs:annotation>
            <xs:documentation>
            The instance_effect element declares the instantiation of a COLLADA effect resource.
            </xs:documentation>
        </xs:annotation>
        <xs:complexType>
            <xs:sequence>
                <xs:element name="technique_hint" minOccurs="0" maxOccurs="unbounded">
                    <xs:annotation>
                        <xs:documentation>
                        Add a hint for a platform of which technique to use in this effect.
                        </xs:documentation>
                    </xs:annotation>
                    <xs:complexType>
                        <xs:attribute name="platform" type="xs:NCName" use="optional">
                            <xs:annotation>
                                <xs:documentation>
                                A platform defines a string that specifies which platform this is hint is aimed for.
                                </xs:documentation>
                            </xs:annotation>
                        </xs:attribute>
                        <xs:attribute name="profile" type="xs:NCName" use="optional">
                            <xs:annotation>
                                <xs:documentation>
                                A profile defines a string that specifies which API profile this is hint is aimed for.
                                </xs:documentation>
                            </xs:annotation>
                        </xs:attribute>
                        <xs:attribute name="ref" type="xs:NCName" use="required">
                            <xs:annotation>
                                <xs:documentation>
                                A reference to the technique to use for the specified platform.
                                </xs:documentation>
                            </xs:annotation>
                        </xs:attribute>
                    </xs:complexType>
                </xs:element>
                <xs:element name="setparam" minOccurs="0" maxOccurs="unbounded">
                    <xs:annotation>
                        <xs:documentation>
                        Assigns a new value to a previously defined parameter
                        </xs:documentation>
                    </xs:annotation>
                    <xs:complexType>
                        <xs:sequence>
                            <xs:group ref="fx_basic_type_common"/>
                        </xs:sequence>
                        <xs:attribute name="ref" type="xs:token" use="required"/>
                    </xs:complexType>
                </xs:element>
                <xs:element ref="extra" minOccurs="0" maxOccurs="unbounded">
                    <xs:annotation>
                        <xs:documentation>
                        The extra element may appear any number of times.
                        </xs:documentation>
                    </xs:annotation>
                </xs:element>
            </xs:sequence>
            <xs:attribute name="url" type="xs:anyURI" use="required">
                <xs:annotation>
                    <xs:documentation>
                    The url attribute refers to resource.  This may refer to a local resource using a relative URL
                    fragment identifier that begins with the “#” character. The url attribute may refer to an external
                    resource using an absolute or relative URL.
                    </xs:documentation>
                </xs:annotation>
            </xs:attribute>
            <xs:attribute name="sid" type="xs:NCName">
                <xs:annotation>
                    <xs:documentation>
                    The sid attribute is a text string value containing the sub-identifier of this element. This
                    value must be unique within the scope of the parent element. Optional attribute.
                    </xs:documentation>
                </xs:annotation>
            </xs:attribute>
            <xs:attribute name="name" type="xs:NCName">
                <xs:annotation>
                    <xs:documentation>
                    The name attribute is the text string name of this element. Optional attribute.
                    </xs:documentation>
                </xs:annotation>
            </xs:attribute>
        </xs:complexType>
    </xs:element>
    <xs:element name="instance_force_field" type="InstanceWithExtra">
        <xs:annotation>
            <xs:documentation>
            The instance_force_field element declares the instantiation of a COLLADA force_field resource.
            </xs:documentation>
        </xs:annotation>
    </xs:element>
    <xs:element name="instance_geometry">
        <xs:annotation>
            <xs:documentation>
            The instance_geometry element declares the instantiation of a COLLADA geometry resource.
            </xs:documentation>
        </xs:annotation>
        <xs:complexType>
            <xs:sequence>
                <xs:element ref="bind_material" minOccurs="0">
                    <xs:annotation>
                        <xs:documentation>
                        Bind a specific material to a piece of geometry, binding varying and uniform parameters at the
                        same time.
                        </xs:documentation>
                    </xs:annotation>
                </xs:element>
                <xs:element ref="extra" minOccurs="0" maxOccurs="unbounded">
                    <xs:annotation>
                        <xs:documentation>
                        The extra element may appear any number of times.
                        </xs:documentation>
                    </xs:annotation>
                </xs:element>
            </xs:sequence>
            <xs:attribute name="url" type="xs:anyURI" use="required">
                <xs:annotation>
                    <xs:documentation>
                    The url attribute refers to resource.  This may refer to a local resource using a relative URL
                    fragment identifier that begins with the “#” character. The url attribute may refer to an external
                    resource using an absolute or relative URL.
                    </xs:documentation>
                </xs:annotation>
            </xs:attribute>
            <xs:attribute name="sid" type="xs:NCName">
                <xs:annotation>
                    <xs:documentation>
                    The sid attribute is a text string value containing the sub-identifier of this element. This
                    value must be unique within the scope of the parent element. Optional attribute.
                    </xs:documentation>
                </xs:annotation>
            </xs:attribute>
            <xs:attribute name="name" type="xs:NCName">
                <xs:annotation>
                    <xs:documentation>
                    The name attribute is the text string name of this element. Optional attribute.
                    </xs:documentation>
                </xs:annotation>
            </xs:attribute>
        </xs:complexType>
    </xs:element>
    <xs:element name="instance_light" type="InstanceWithExtra">
        <xs:annotation>
            <xs:documentation>
            The instance_light element declares the instantiation of a COLLADA light resource.
            </xs:documentation>
        </xs:annotation>
    </xs:element>
    <xs:element name="instance_material">
        <xs:annotation>
            <xs:documentation>
            The instance_material element declares the instantiation of a COLLADA material resource.
            </xs:documentation>
        </xs:annotation>
        <xs:complexType>
            <xs:sequence>
                <xs:element name="bind" minOccurs="0" maxOccurs="unbounded">
                    <xs:annotation>
                        <xs:documentation>
                        The bind element binds values to effect parameters upon instantiation.
                        </xs:documentation>
                    </xs:annotation>
                    <xs:complexType>
                        <xs:attribute name="semantic" type="xs:NCName" use="required">
                            <xs:annotation>
                                <xs:documentation>
                                The semantic attribute specifies which effect parameter to bind.
                                </xs:documentation>
                            </xs:annotation>
                        </xs:attribute>
                        <xs:attribute name="target" type="xs:token" use="required">
                            <xs:annotation>
                                <xs:documentation>
                                The target attribute specifies the location of the value to bind to the specified semantic.
                                This text string is a path-name following a simple syntax described in the “Addressing Syntax”
                                section.
                                </xs:documentation>
                            </xs:annotation>
                        </xs:attribute>
                    </xs:complexType>
                </xs:element>
                <xs:element name="bind_vertex_input" minOccurs="0" maxOccurs="unbounded">
                    <xs:annotation>
                        <xs:documentation>
                        The bind_vertex_input element binds vertex inputs to effect parameters upon instantiation.
                        </xs:documentation>
                    </xs:annotation>
                    <xs:complexType>
                        <xs:attribute name="semantic" type="xs:NCName" use="required">
                            <xs:annotation>
                                <xs:documentation>
                                The semantic attribute specifies which effect parameter to bind.
                                </xs:documentation>
                            </xs:annotation>
                        </xs:attribute>
                        <xs:attribute name="input_semantic" type="xs:NCName" use="required">
                            <xs:annotation>
                                <xs:documentation>
                                The input_semantic attribute specifies which input semantic to bind.
                                </xs:documentation>
                            </xs:annotation>
                        </xs:attribute>
                        <xs:attribute name="input_set" type="uint">
                            <xs:annotation>
                                <xs:documentation>
                                The input_set attribute specifies which input set to bind.
                                </xs:documentation>
                            </xs:annotation>
                        </xs:attribute>
                    </xs:complexType>
                </xs:element>
                <xs:element ref="extra" minOccurs="0" maxOccurs="unbounded">
                    <xs:annotation>
                        <xs:documentation>
                        The extra element may appear any number of times.
                        </xs:documentation>
                    </xs:annotation>
                </xs:element>
            </xs:sequence>
            <xs:attribute name="symbol" type="xs:NCName" use="required">
                <xs:annotation>
                    <xs:documentation>
                    The symbol attribute specifies which symbol defined from within the geometry this material binds to.
                    </xs:documentation>
                </xs:annotation>
            </xs:attribute>
            <xs:attribute name="target" type="xs:anyURI" use="required">
                <xs:annotation>
                    <xs:documentation>
                    The target attribute specifies the URL of the location of the object to instantiate.
                    </xs:documentation>
                </xs:annotation>
            </xs:attribute>
            <xs:attribute name="sid" type="xs:NCName">
                <xs:annotation>
                    <xs:documentation>
                    The sid attribute is a text string value containing the sub-identifier of this element. This
                    value must be unique within the scope of the parent element. Optional attribute.
                    </xs:documentation>
                </xs:annotation>
            </xs:attribute>
            <xs:attribute name="name" type="xs:NCName">
                <xs:annotation>
                    <xs:documentation>
                    The name attribute is the text string name of this element. Optional attribute.
                    </xs:documentation>
                </xs:annotation>
            </xs:attribute>
        </xs:complexType>
    </xs:element>
    <xs:element name="instance_node" type="InstanceWithExtra">
        <xs:annotation>
            <xs:documentation>
            The instance_node element declares the instantiation of a COLLADA node resource.
            </xs:documentation>
        </xs:annotation>
    </xs:element>
    <xs:element name="instance_physics_material" type="InstanceWithExtra">
        <xs:annotation>
            <xs:documentation>
            The instance_physics_material element declares the instantiation of a COLLADA physics_material
            resource.
            </xs:documentation>
        </xs:annotation>
    </xs:element>
    <xs:element name="instance_physics_model">
        <xs:annotation>
            <xs:documentation>
            This element allows instancing physics model within another physics model, or in a physics scene.
            </xs:documentation>
        </xs:annotation>
        <xs:complexType>
            <xs:sequence>
                <xs:element ref="instance_force_field" minOccurs="0" maxOccurs="unbounded">
                    <xs:annotation>
                        <xs:documentation>
                        The instance_physics_model element may instance any number of force_field elements.
                        </xs:documentation>
                    </xs:annotation>
                </xs:element>
                <xs:element ref="instance_rigid_body" minOccurs="0" maxOccurs="unbounded">
                    <xs:annotation>
                        <xs:documentation>
                        The instance_physics_model element may instance any number of rigid_body elements.
                        </xs:documentation>
                    </xs:annotation>
                </xs:element>
                <xs:element ref="instance_rigid_constraint" minOccurs="0" maxOccurs="unbounded">
                    <xs:annotation>
                        <xs:documentation>
                        The instance_physics_model element may instance any number of rigid_constraint elements.
                        </xs:documentation>
                    </xs:annotation>
                </xs:element>
                <xs:element ref="extra" minOccurs="0" maxOccurs="unbounded">
                    <xs:annotation>
                        <xs:documentation>
                        The extra element may appear any number of times.
                        </xs:documentation>
                    </xs:annotation>
                </xs:element>
            </xs:sequence>
            <xs:attribute name="url" type="xs:anyURI" use="required">
                <xs:annotation>
                    <xs:documentation>
                    The url attribute refers to resource.  This may refer to a local resource using a relative URL
                    fragment identifier that begins with the “#” character. The url attribute may refer to an external
                    resource using an absolute or relative URL.
                    </xs:documentation>
                </xs:annotation>
            </xs:attribute>
            <xs:attribute name="sid" type="xs:NCName">
                <xs:annotation>
                    <xs:documentation>
                    The sid attribute is a text string value containing the sub-identifier of this element. This
                    value must be unique within the scope of the parent element. Optional attribute.
                    </xs:documentation>
                </xs:annotation>
            </xs:attribute>
            <xs:attribute name="name" type="xs:NCName">
                <xs:annotation>
                    <xs:documentation>
                    The name attribute is the text string name of this element. Optional attribute.
                    </xs:documentation>
                </xs:annotation>
            </xs:attribute>
            <xs:attribute name="parent" type="xs:anyURI">
                <xs:annotation>
                    <xs:documentation>
                    The parent attribute points to the id of a node in the visual scene. This allows a physics model
                    to be instantiated under a specific transform node, which will dictate the initial position and
                    orientation, and could be animated to influence kinematic rigid bodies.
                    </xs:documentation>
                </xs:annotation>
            </xs:attribute>
        </xs:complexType>
    </xs:element>
    <xs:element name="instance_rigid_body">
        <xs:annotation>
            <xs:documentation>
            This element allows instancing a rigid_body within an instance_physics_model.
            </xs:documentation>
        </xs:annotation>
        <xs:complexType>
            <xs:sequence>
                <xs:element name="technique_common">
                    <xs:annotation>
                        <xs:documentation>
                        The technique_common element specifies the instance_rigid_body information for the common
                        profile which all COLLADA implementations need to support.
                        </xs:documentation>
                    </xs:annotation>
                    <xs:complexType>
                        <xs:sequence>
                            <xs:element name="angular_velocity" type="float3" default="0.0 0.0 0.0" minOccurs="0">
                                <xs:annotation>
                                    <xs:documentation>
                                    Specifies the initial angular velocity of the rigid_body instance in degrees per second
                                    around each axis, in the form of an X-Y-Z Euler rotation.
                                    </xs:documentation>
                                </xs:annotation>
                            </xs:element>
                            <xs:element name="velocity" type="float3" default="0.0 0.0 0.0" minOccurs="0">
                                <xs:annotation>
                                    <xs:documentation>
                                    Specifies the initial linear velocity of the rigid_body instance.
                                    </xs:documentation>
                                </xs:annotation>
                            </xs:element>
                            <xs:element name="dynamic" minOccurs="0">
                                <xs:complexType>
                                    <xs:simpleContent>
                                        <xs:extension base="bool">
                                            <xs:attribute name="sid" type="xs:NCName">
                                                <xs:annotation>
                                                    <xs:documentation>
                                                    The sid attribute is a text string value containing the sub-identifier of this element.
                                                    This value must be unique within the scope of the parent element. Optional attribute.
                                                    </xs:documentation>
                                                </xs:annotation>
                                            </xs:attribute>
                                        </xs:extension>
                                    </xs:simpleContent>
                                </xs:complexType>
                            </xs:element>
                            <xs:element name="mass" type="TargetableFloat" minOccurs="0"/>
                            <xs:element name="mass_frame" minOccurs="0">
                                <xs:complexType>
                                    <xs:choice maxOccurs="unbounded">
                                        <xs:element ref="translate"/>
                                        <xs:element ref="rotate"/>
                                    </xs:choice>
                                </xs:complexType>
                            </xs:element>
                            <xs:element name="inertia" type="TargetableFloat3" minOccurs="0"/>
                            <xs:choice minOccurs="0">
                                <xs:element ref="instance_physics_material"/>
                                <xs:element ref="physics_material"/>
                            </xs:choice>
                            <xs:element name="shape" minOccurs="0" maxOccurs="unbounded">
                                <xs:complexType>
                                    <xs:sequence>
                                        <xs:element name="hollow" minOccurs="0">
                                            <xs:complexType>
                                                <xs:simpleContent>
                                                    <xs:extension base="bool">
                                                        <xs:attribute name="sid" type="xs:NCName">
                                                            <xs:annotation>
                                                                <xs:documentation>
                                                                The sid attribute is a text string value containing the sub-identifier of this element. This value must be unique within the scope of the parent element. Optional attribute.
                                                                </xs:documentation>
                                                            </xs:annotation>
                                                        </xs:attribute>
                                                    </xs:extension>
                                                </xs:simpleContent>
                                            </xs:complexType>
                                        </xs:element>
                                        <xs:element name="mass" type="TargetableFloat" minOccurs="0"/>
                                        <xs:element name="density" type="TargetableFloat" minOccurs="0"/>
                                        <xs:choice minOccurs="0">
                                            <xs:element ref="instance_physics_material"/>
                                            <xs:element ref="physics_material"/>
                                        </xs:choice>
                                        <xs:choice>
                                            <xs:element ref="instance_geometry"/>
                                            <xs:element ref="plane"/>
                                            <xs:element ref="box"/>
                                            <xs:element ref="sphere"/>
                                            <xs:element ref="cylinder"/>
                                            <xs:element ref="tapered_cylinder"/>
                                            <xs:element ref="capsule"/>
                                            <xs:element ref="tapered_capsule"/>
                                        </xs:choice>
                                        <xs:choice minOccurs="0" maxOccurs="unbounded">
                                            <xs:element ref="translate"/>
                                            <xs:element ref="rotate"/>
                                        </xs:choice>
                                        <xs:element ref="extra" minOccurs="0" maxOccurs="unbounded">
                                            <xs:annotation>
                                                <xs:documentation>
                                                The extra element may appear any number of times.
                                                </xs:documentation>
                                            </xs:annotation>
                                        </xs:element>
                                    </xs:sequence>
                                </xs:complexType>
                            </xs:element>
                        </xs:sequence>
                    </xs:complexType>
                </xs:element>
                <xs:element ref="technique" minOccurs="0" maxOccurs="unbounded">
                    <xs:annotation>
                        <xs:documentation>
                        This element may contain any number of non-common profile techniques.
                        </xs:documentation>
                    </xs:annotation>
                </xs:element>
                <xs:element ref="extra" minOccurs="0" maxOccurs="unbounded">
                    <xs:annotation>
                        <xs:documentation>
                        The extra element may appear any number of times.
                        </xs:documentation>
                    </xs:annotation>
                </xs:element>
            </xs:sequence>
            <xs:attribute name="body" type="xs:NCName" use="required">
                <xs:annotation>
                    <xs:documentation>
                    The body attribute indicates which rigid_body to instantiate. Required attribute.
                    </xs:documentation>
                </xs:annotation>
            </xs:attribute>
            <xs:attribute name="sid" type="xs:NCName">
                <xs:annotation>
                    <xs:documentation>
                    The sid attribute is a text string value containing the sub-identifier of this element. This
                    value must be unique within the scope of the parent element. Optional attribute.
                    </xs:documentation>
                </xs:annotation>
            </xs:attribute>
            <xs:attribute name="name" type="xs:NCName">
                <xs:annotation>
                    <xs:documentation>
                    The name attribute is the text string name of this element. Optional attribute.
                    </xs:documentation>
                </xs:annotation>
            </xs:attribute>
            <xs:attribute name="target" type="xs:anyURI" use="required">
                <xs:annotation>
                    <xs:documentation>
                    The target attribute indicates which node is influenced by this rigid_body instance.
                    Required attribute
                    </xs:documentation>
                </xs:annotation>
            </xs:attribute>
        </xs:complexType>
    </xs:element>
    <xs:element name="instance_rigid_constraint">
        <xs:annotation>
            <xs:documentation>
            This element allows instancing a rigid_constraint within an instance_physics_model.
            </xs:documentation>
        </xs:annotation>
        <xs:complexType>
            <xs:sequence>
                <xs:element ref="extra" minOccurs="0" maxOccurs="unbounded">
                    <xs:annotation>
                        <xs:documentation>
                        The extra element may appear any number of times.
                        </xs:documentation>
                    </xs:annotation>
                </xs:element>
            </xs:sequence>
            <xs:attribute name="constraint" type="xs:NCName" use="required">
                <xs:annotation>
                    <xs:documentation>
                    The constraint attribute indicates which rigid_constraing to instantiate. Required attribute.
                    </xs:documentation>
                </xs:annotation>
            </xs:attribute>
            <xs:attribute name="sid" type="xs:NCName">
                <xs:annotation>
                    <xs:documentation>
                    The sid attribute is a text string value containing the sub-identifier of this element. This
                    value must be unique within the scope of the parent element. Optional attribute.
                    </xs:documentation>
                </xs:annotation>
            </xs:attribute>
            <xs:attribute name="name" type="xs:NCName">
                <xs:annotation>
                    <xs:documentation>
                    The name attribute is the text string name of this element. Optional attribute.
                    </xs:documentation>
                </xs:annotation>
            </xs:attribute>
        </xs:complexType>
    </xs:element>
    <!-- Modularity elements -->
    <xs:element name="library_animations">
        <xs:annotation>
            <xs:documentation>
            The library_animations element declares a module of animation elements.
            </xs:documentation>
        </xs:annotation>
        <xs:complexType>
            <xs:sequence>
                <xs:element ref="asset" minOccurs="0">
                    <xs:annotation>
                        <xs:documentation>
                        The library_animations element may contain an asset element.
                        </xs:documentation>
                    </xs:annotation>
                </xs:element>
                <xs:element ref="animation" maxOccurs="unbounded">
                    <xs:annotation>
                        <xs:documentation>
                        There must be at least one animation element.
                        </xs:documentation>
                    </xs:annotation>
                </xs:element>
                <xs:element ref="extra" minOccurs="0" maxOccurs="unbounded">
                    <xs:annotation>
                        <xs:documentation>
                        The extra element may appear any number of times.
                        </xs:documentation>
                    </xs:annotation>
                </xs:element>
            </xs:sequence>
            <xs:attribute name="id" type="xs:ID">
                <xs:annotation>
                    <xs:documentation>
                    The id attribute is a text string containing the unique identifier of this element.
                    This value must be unique within the instance document. Optional attribute.
                    </xs:documentation>
                </xs:annotation>
            </xs:attribute>
            <xs:attribute name="name" type="xs:NCName">
                <xs:annotation>
                    <xs:documentation>
                    The name attribute is the text string name of this element. Optional attribute.
                    </xs:documentation>
                </xs:annotation>
            </xs:attribute>
        </xs:complexType>
    </xs:element>
    <xs:element name="library_animation_clips">
        <xs:annotation>
            <xs:documentation>
            The library_animation_clips element declares a module of animation_clip elements.
            </xs:documentation>
        </xs:annotation>
        <xs:complexType>
            <xs:sequence>
                <xs:element ref="asset" minOccurs="0">
                    <xs:annotation>
                        <xs:documentation>
                        The library_animation_clips element may contain an asset element.
                        </xs:documentation>
                    </xs:annotation>
                </xs:element>
                <xs:element ref="animation_clip" maxOccurs="unbounded">
                    <xs:annotation>
                        <xs:documentation>
                        There must be at least one animation_clip element.
                        </xs:documentation>
                    </xs:annotation>
                </xs:element>
                <xs:element ref="extra" minOccurs="0" maxOccurs="unbounded">
                    <xs:annotation>
                        <xs:documentation>
                        The extra element may appear any number of times.
                        </xs:documentation>
                    </xs:annotation>
                </xs:element>
            </xs:sequence>
            <xs:attribute name="id" type="xs:ID">
                <xs:annotation>
                    <xs:documentation>
                    The id attribute is a text string containing the unique identifier of this element.
                    This value must be unique within the instance document. Optional attribute.
                    </xs:documentation>
                </xs:annotation>
            </xs:attribute>
            <xs:attribute name="name" type="xs:NCName">
                <xs:annotation>
                    <xs:documentation>
                    The name attribute is the text string name of this element. Optional attribute.
                    </xs:documentation>
                </xs:annotation>
            </xs:attribute>
        </xs:complexType>
    </xs:element>
    <xs:element name="library_cameras">
        <xs:annotation>
            <xs:documentation>
            The library_cameras element declares a module of camera elements.
            </xs:documentation>
        </xs:annotation>
        <xs:complexType>
            <xs:sequence>
                <xs:element ref="asset" minOccurs="0">
                    <xs:annotation>
                        <xs:documentation>
                        The library_cameras element may contain an asset element.
                        </xs:documentation>
                    </xs:annotation>
                </xs:element>
                <xs:element ref="camera" maxOccurs="unbounded">
                    <xs:annotation>
                        <xs:documentation>
                        There must be at least one camera element.
                        </xs:documentation>
                    </xs:annotation>
                </xs:element>
                <xs:element ref="extra" minOccurs="0" maxOccurs="unbounded">
                    <xs:annotation>
                        <xs:documentation>
                        The extra element may appear any number of times.
                        </xs:documentation>
                    </xs:annotation>
                </xs:element>
            </xs:sequence>
            <xs:attribute name="id" type="xs:ID">
                <xs:annotation>
                    <xs:documentation>
                    The id attribute is a text string containing the unique identifier of this element.
                    This value must be unique within the instance document. Optional attribute.
                    </xs:documentation>
                </xs:annotation>
            </xs:attribute>
            <xs:attribute name="name" type="xs:NCName">
                <xs:annotation>
                    <xs:documentation>
                    The name attribute is the text string name of this element. Optional attribute.
                    </xs:documentation>
                </xs:annotation>
            </xs:attribute>
        </xs:complexType>
    </xs:element>
    <xs:element name="library_controllers">
        <xs:annotation>
            <xs:documentation>
            The library_controllers element declares a module of controller elements.
            </xs:documentation>
        </xs:annotation>
        <xs:complexType>
            <xs:sequence>
                <xs:element ref="asset" minOccurs="0">
                    <xs:annotation>
                        <xs:documentation>
                        The library_controllers element may contain an asset element.
                        </xs:documentation>
                    </xs:annotation>
                </xs:element>
                <xs:element ref="controller" maxOccurs="unbounded">
                    <xs:annotation>
                        <xs:documentation>
                        There must be at least one controller element.
                        </xs:documentation>
                    </xs:annotation>
                </xs:element>
                <xs:element ref="extra" minOccurs="0" maxOccurs="unbounded">
                    <xs:annotation>
                        <xs:documentation>
                        The extra element may appear any number of times.
                        </xs:documentation>
                    </xs:annotation>
                </xs:element>
            </xs:sequence>
            <xs:attribute name="id" type="xs:ID">
                <xs:annotation>
                    <xs:documentation>
                    The id attribute is a text string containing the unique identifier of this element.
                    This value must be unique within the instance document. Optional attribute.
                    </xs:documentation>
                </xs:annotation>
            </xs:attribute>
            <xs:attribute name="name" type="xs:NCName">
                <xs:annotation>
                    <xs:documentation>
                    The name attribute is the text string name of this element. Optional attribute.
                    </xs:documentation>
                </xs:annotation>
            </xs:attribute>
        </xs:complexType>
    </xs:element>
    <xs:element name="library_geometries">
        <xs:annotation>
            <xs:documentation>
            The library_geometries element declares a module of geometry elements.
            </xs:documentation>
        </xs:annotation>
        <xs:complexType>
            <xs:sequence>
                <xs:element ref="asset" minOccurs="0">
                    <xs:annotation>
                        <xs:documentation>
                        The library_geometries element may contain an asset element.
                        </xs:documentation>
                    </xs:annotation>
                </xs:element>
                <xs:element ref="geometry" maxOccurs="unbounded">
                    <xs:annotation>
                        <xs:documentation>
                        There must be at least one geometry element.
                        </xs:documentation>
                    </xs:annotation>
                </xs:element>
                <xs:element ref="extra" minOccurs="0" maxOccurs="unbounded">
                    <xs:annotation>
                        <xs:documentation>
                        The extra element may appear any number of times.
                        </xs:documentation>
                    </xs:annotation>
                </xs:element>
            </xs:sequence>
            <xs:attribute name="id" type="xs:ID">
                <xs:annotation>
                    <xs:documentation>
                    The id attribute is a text string containing the unique identifier of this element.
                    This value must be unique within the instance document. Optional attribute.
                    </xs:documentation>
                </xs:annotation>
            </xs:attribute>
            <xs:attribute name="name" type="xs:NCName">
                <xs:annotation>
                    <xs:documentation>
                    The name attribute is the text string name of this element. Optional attribute.
                    </xs:documentation>
                </xs:annotation>
            </xs:attribute>
        </xs:complexType>
    </xs:element>
    <xs:element name="library_effects">
        <xs:annotation>
            <xs:documentation>
            The library_effects element declares a module of effect elements.
            </xs:documentation>
        </xs:annotation>
        <xs:complexType>
            <xs:sequence>
                <xs:element ref="asset" minOccurs="0">
                    <xs:annotation>
                        <xs:documentation>
                        The library_effects element may contain an asset element.
                        </xs:documentation>
                    </xs:annotation>
                </xs:element>
                <xs:element ref="effect" maxOccurs="unbounded">
                    <xs:annotation>
                        <xs:documentation>
                        There must be at least one effect element.
                        </xs:documentation>
                    </xs:annotation>
                </xs:element>
                <xs:element ref="extra" minOccurs="0" maxOccurs="unbounded">
                    <xs:annotation>
                        <xs:documentation>
                        The extra element may appear any number of times.
                        </xs:documentation>
                    </xs:annotation>
                </xs:element>
            </xs:sequence>
            <xs:attribute name="id" type="xs:ID">
                <xs:annotation>
                    <xs:documentation>
                    The id attribute is a text string containing the unique identifier of this element.
                    This value must be unique within the instance document. Optional attribute.
                    </xs:documentation>
                </xs:annotation>
            </xs:attribute>
            <xs:attribute name="name" type="xs:NCName">
                <xs:annotation>
                    <xs:documentation>
                    The name attribute is the text string name of this element. Optional attribute.
                    </xs:documentation>
                </xs:annotation>
            </xs:attribute>
        </xs:complexType>
    </xs:element>
    <xs:element name="library_force_fields">
        <xs:annotation>
            <xs:documentation>
            The library_force_fields element declares a module of force_field elements.
            </xs:documentation>
        </xs:annotation>
        <xs:complexType>
            <xs:sequence>
                <xs:element ref="asset" minOccurs="0">
                    <xs:annotation>
                        <xs:documentation>
                        The library_force_fields element may contain an asset element.
                        </xs:documentation>
                    </xs:annotation>
                </xs:element>
                <xs:element ref="force_field" maxOccurs="unbounded">
                    <xs:annotation>
                        <xs:documentation>
                        There must be at least one force_field element.
                        </xs:documentation>
                    </xs:annotation>
                </xs:element>
                <xs:element ref="extra" minOccurs="0" maxOccurs="unbounded">
                    <xs:annotation>
                        <xs:documentation>
                        The extra element may appear any number of times.
                        </xs:documentation>
                    </xs:annotation>
                </xs:element>
            </xs:sequence>
            <xs:attribute name="id" type="xs:ID">
                <xs:annotation>
                    <xs:documentation>
                    The id attribute is a text string containing the unique identifier of this element.
                    This value must be unique within the instance document. Optional attribute.
                    </xs:documentation>
                </xs:annotation>
            </xs:attribute>
            <xs:attribute name="name" type="xs:NCName">
                <xs:annotation>
                    <xs:documentation>
                    The name attribute is the text string name of this element. Optional attribute.
                    </xs:documentation>
                </xs:annotation>
            </xs:attribute>
        </xs:complexType>
    </xs:element>
    <xs:element name="library_images">
        <xs:annotation>
            <xs:documentation>
            The library_images element declares a module of image elements.
            </xs:documentation>
        </xs:annotation>
        <xs:complexType>
            <xs:sequence>
                <xs:element ref="asset" minOccurs="0">
                    <xs:annotation>
                        <xs:documentation>
                        The library_images element may contain an asset element.
                        </xs:documentation>
                    </xs:annotation>
                </xs:element>
                <xs:element ref="image" maxOccurs="unbounded">
                    <xs:annotation>
                        <xs:documentation>
                        There must be at least one image element.
                        </xs:documentation>
                    </xs:annotation>
                </xs:element>
                <xs:element ref="extra" minOccurs="0" maxOccurs="unbounded">
                    <xs:annotation>
                        <xs:documentation>
                        The extra element may appear any number of times.
                        </xs:documentation>
                    </xs:annotation>
                </xs:element>
            </xs:sequence>
            <xs:attribute name="id" type="xs:ID">
                <xs:annotation>
                    <xs:documentation>
                    The id attribute is a text string containing the unique identifier of this element.
                    This value must be unique within the instance document. Optional attribute.
                    </xs:documentation>
                </xs:annotation>
            </xs:attribute>
            <xs:attribute name="name" type="xs:NCName">
                <xs:annotation>
                    <xs:documentation>
                    The name attribute is the text string name of this element. Optional attribute.
                    </xs:documentation>
                </xs:annotation>
            </xs:attribute>
        </xs:complexType>
    </xs:element>
    <xs:element name="library_lights">
        <xs:annotation>
            <xs:documentation>
            The library_lights element declares a module of light elements.
            </xs:documentation>
        </xs:annotation>
        <xs:complexType>
            <xs:sequence>
                <xs:element ref="asset" minOccurs="0">
                    <xs:annotation>
                        <xs:documentation>
                        The library_lights element may contain an asset element.
                        </xs:documentation>
                    </xs:annotation>
                </xs:element>
                <xs:element ref="light" maxOccurs="unbounded">
                    <xs:annotation>
                        <xs:documentation>
                        There must be at least one light element.
                        </xs:documentation>
                    </xs:annotation>
                </xs:element>
                <xs:element ref="extra" minOccurs="0" maxOccurs="unbounded">
                    <xs:annotation>
                        <xs:documentation>
                        The extra element may appear any number of times.
                        </xs:documentation>
                    </xs:annotation>
                </xs:element>
            </xs:sequence>
            <xs:attribute name="id" type="xs:ID">
                <xs:annotation>
                    <xs:documentation>
                    The id attribute is a text string containing the unique identifier of this element.
                    This value must be unique within the instance document. Optional attribute.
                    </xs:documentation>
                </xs:annotation>
            </xs:attribute>
            <xs:attribute name="name" type="xs:NCName">
                <xs:annotation>
                    <xs:documentation>
                    The name attribute is the text string name of this element. Optional attribute.
                    </xs:documentation>
                </xs:annotation>
            </xs:attribute>
        </xs:complexType>
    </xs:element>
    <xs:element name="library_materials">
        <xs:annotation>
            <xs:documentation>
            The library_materials element declares a module of material elements.
            </xs:documentation>
        </xs:annotation>
        <xs:complexType>
            <xs:sequence>
                <xs:element ref="asset" minOccurs="0">
                    <xs:annotation>
                        <xs:documentation>
                        The library_materials element may contain an asset element.
                        </xs:documentation>
                    </xs:annotation>
                </xs:element>
                <xs:element ref="material" maxOccurs="unbounded">
                    <xs:annotation>
                        <xs:documentation>
                        There must be at least one material element.
                        </xs:documentation>
                    </xs:annotation>
                </xs:element>
                <xs:element ref="extra" minOccurs="0" maxOccurs="unbounded">
                    <xs:annotation>
                        <xs:documentation>
                        The extra element may appear any number of times.
                        </xs:documentation>
                    </xs:annotation>
                </xs:element>
            </xs:sequence>
            <xs:attribute name="id" type="xs:ID">
                <xs:annotation>
                    <xs:documentation>
                    The id attribute is a text string containing the unique identifier of this element.
                    This value must be unique within the instance document. Optional attribute.
                    </xs:documentation>
                </xs:annotation>
            </xs:attribute>
            <xs:attribute name="name" type="xs:NCName">
                <xs:annotation>
                    <xs:documentation>
                    The name attribute is the text string name of this element. Optional attribute.
                    </xs:documentation>
                </xs:annotation>
            </xs:attribute>
        </xs:complexType>
    </xs:element>
    <xs:element name="library_nodes">
        <xs:annotation>
            <xs:documentation>
            The library_nodes element declares a module of node elements.
            </xs:documentation>
        </xs:annotation>
        <xs:complexType>
            <xs:sequence>
                <xs:element ref="asset" minOccurs="0">
                    <xs:annotation>
                        <xs:documentation>
                        The library_nodes element may contain an asset element.
                        </xs:documentation>
                    </xs:annotation>
                </xs:element>
                <xs:element ref="node" maxOccurs="unbounded">
                    <xs:annotation>
                        <xs:documentation>
                        There must be at least one node element.
                        </xs:documentation>
                    </xs:annotation>
                </xs:element>
                <xs:element ref="extra" minOccurs="0" maxOccurs="unbounded">
                    <xs:annotation>
                        <xs:documentation>
                        The extra element may appear any number of times.
                        </xs:documentation>
                    </xs:annotation>
                </xs:element>
            </xs:sequence>
            <xs:attribute name="id" type="xs:ID">
                <xs:annotation>
                    <xs:documentation>
                    The id attribute is a text string containing the unique identifier of this element.
                    This value must be unique within the instance document. Optional attribute.
                    </xs:documentation>
                </xs:annotation>
            </xs:attribute>
            <xs:attribute name="name" type="xs:NCName">
                <xs:annotation>
                    <xs:documentation>
                    The name attribute is the text string name of this element. Optional attribute.
                    </xs:documentation>
                </xs:annotation>
            </xs:attribute>
        </xs:complexType>
    </xs:element>
    <xs:element name="library_physics_materials">
        <xs:annotation>
            <xs:documentation>
            The library_physics_materials element declares a module of physics_material elements.
            </xs:documentation>
        </xs:annotation>
        <xs:complexType>
            <xs:sequence>
                <xs:element ref="asset" minOccurs="0">
                    <xs:annotation>
                        <xs:documentation>
                        The library_physics_materials element may contain an asset element.
                        </xs:documentation>
                    </xs:annotation>
                </xs:element>
                <xs:element ref="physics_material" maxOccurs="unbounded">
                    <xs:annotation>
                        <xs:documentation>
                        There must be at least one physics_material element.
                        </xs:documentation>
                    </xs:annotation>
                </xs:element>
                <xs:element ref="extra" minOccurs="0" maxOccurs="unbounded">
                    <xs:annotation>
                        <xs:documentation>
                        The extra element may appear any number of times.
                        </xs:documentation>
                    </xs:annotation>
                </xs:element>
            </xs:sequence>
            <xs:attribute name="id" type="xs:ID">
                <xs:annotation>
                    <xs:documentation>
                    The id attribute is a text string containing the unique identifier of this element.
                    This value must be unique within the instance document. Optional attribute.
                    </xs:documentation>
                </xs:annotation>
            </xs:attribute>
            <xs:attribute name="name" type="xs:NCName">
                <xs:annotation>
                    <xs:documentation>
                    The name attribute is the text string name of this element. Optional attribute.
                    </xs:documentation>
                </xs:annotation>
            </xs:attribute>
        </xs:complexType>
    </xs:element>
    <xs:element name="library_physics_models">
        <xs:annotation>
            <xs:documentation>
            The library_physics_models element declares a module of physics_model elements.
            </xs:documentation>
        </xs:annotation>
        <xs:complexType>
            <xs:sequence>
                <xs:element ref="asset" minOccurs="0">
                    <xs:annotation>
                        <xs:documentation>
                        The library_physics_models element may contain an asset element.
                        </xs:documentation>
                    </xs:annotation>
                </xs:element>
                <xs:element ref="physics_model" maxOccurs="unbounded">
                    <xs:annotation>
                        <xs:documentation>
                        There must be at least one physics_model element.
                        </xs:documentation>
                    </xs:annotation>
                </xs:element>
                <xs:element ref="extra" minOccurs="0" maxOccurs="unbounded">
                    <xs:annotation>
                        <xs:documentation>
                        The extra element may appear any number of times.
                        </xs:documentation>
                    </xs:annotation>
                </xs:element>
            </xs:sequence>
            <xs:attribute name="id" type="xs:ID">
                <xs:annotation>
                    <xs:documentation>
                    The id attribute is a text string containing the unique identifier of this element.
                    This value must be unique within the instance document. Optional attribute.
                    </xs:documentation>
                </xs:annotation>
            </xs:attribute>
            <xs:attribute name="name" type="xs:NCName">
                <xs:annotation>
                    <xs:documentation>
                    The name attribute is the text string name of this element. Optional attribute.
                    </xs:documentation>
                </xs:annotation>
            </xs:attribute>
        </xs:complexType>
    </xs:element>
    <xs:element name="library_physics_scenes">
        <xs:annotation>
            <xs:documentation>
            The library_physics_scenes element declares a module of physics_scene elements.
            </xs:documentation>
        </xs:annotation>
        <xs:complexType>
            <xs:sequence>
                <xs:element ref="asset" minOccurs="0">
                    <xs:annotation>
                        <xs:documentation>
                        The library_physics_scenes element may contain an asset element.
                        </xs:documentation>
                    </xs:annotation>
                </xs:element>
                <xs:element ref="physics_scene" maxOccurs="unbounded">
                    <xs:annotation>
                        <xs:documentation>
                        There must be at least one physics_scene element.
                        </xs:documentation>
                    </xs:annotation>
                </xs:element>
                <xs:element ref="extra" minOccurs="0" maxOccurs="unbounded">
                    <xs:annotation>
                        <xs:documentation>
                        The extra element may appear any number of times.
                        </xs:documentation>
                    </xs:annotation>
                </xs:element>
            </xs:sequence>
            <xs:attribute name="id" type="xs:ID">
                <xs:annotation>
                    <xs:documentation>
                    The id attribute is a text string containing the unique identifier of this element.
                    This value must be unique within the instance document. Optional attribute.
                    </xs:documentation>
                </xs:annotation>
            </xs:attribute>
            <xs:attribute name="name" type="xs:NCName">
                <xs:annotation>
                    <xs:documentation>
                    The name attribute is the text string name of this element. Optional attribute.
                    </xs:documentation>
                </xs:annotation>
            </xs:attribute>
        </xs:complexType>
    </xs:element>
    <xs:element name="library_visual_scenes">
        <xs:annotation>
            <xs:documentation>
            The library_visual_scenes element declares a module of visual_scene elements.
            </xs:documentation>
        </xs:annotation>
        <xs:complexType>
            <xs:sequence>
                <xs:element ref="asset" minOccurs="0">
                    <xs:annotation>
                        <xs:documentation>
                        The library_visual_scenes element may contain an asset element.
                        </xs:documentation>
                    </xs:annotation>
                </xs:element>
                <xs:element ref="visual_scene" maxOccurs="unbounded">
                    <xs:annotation>
                        <xs:documentation>
                        There must be at least one visual_scene element.
                        </xs:documentation>
                    </xs:annotation>
                </xs:element>
                <xs:element ref="extra" minOccurs="0" maxOccurs="unbounded">
                    <xs:annotation>
                        <xs:documentation>
                        The extra element may appear any number of times.
                        </xs:documentation>
                    </xs:annotation>
                </xs:element>
            </xs:sequence>
            <xs:attribute name="id" type="xs:ID">
                <xs:annotation>
                    <xs:documentation>
                    The id attribute is a text string containing the unique identifier of this element.
                    This value must be unique within the instance document. Optional attribute.
                    </xs:documentation>
                </xs:annotation>
            </xs:attribute>
            <xs:attribute name="name" type="xs:NCName">
                <xs:annotation>
                    <xs:documentation>
                    The name attribute is the text string name of this element. Optional attribute.
                    </xs:documentation>
                </xs:annotation>
            </xs:attribute>
        </xs:complexType>
    </xs:element>
    <!-- =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=- -->
    <!-- COLLADA FX types in common scope     -->
    <!-- =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=- -->
    <xs:simpleType name="fx_color_common">
        <xs:restriction base="float4"/>
    </xs:simpleType>
    <xs:simpleType name="fx_opaque_enum">
        <xs:restriction base="xs:string">
            <xs:enumeration value="A_ONE">
                <xs:annotation>
                    <xs:documentation>
                        When a transparent opaque attribute is set to A_ONE, it means the transparency information will be taken from the alpha channel of the color, texture, or parameter supplying the value. The value of 1.0 is opaque in this mode.
                    </xs:documentation>
                </xs:annotation>
            </xs:enumeration>
            <xs:enumeration value="RGB_ZERO">
                <xs:annotation>
                    <xs:documentation>
                        When a transparent opaque attribute is set to RGB_ZERO, it means the transparency information will be taken from the red, green, and blue channels of the color, texture, or parameter supplying the value. Each channel is modulated independently. The value of 0.0 is opaque in this mode.
                    </xs:documentation>
                </xs:annotation>
            </xs:enumeration>
        </xs:restriction>
    </xs:simpleType>
    <xs:simpleType name="fx_surface_type_enum">
        <xs:restriction base="xs:string">
            <xs:enumeration value="UNTYPED">
                <xs:annotation>
                    <xs:documentation>
                        When a surface's type attribute is set to UNTYPED, its type is initially unknown and established later by the context in which it is used, such as by a texture sampler that references it. A surface of any other type may be changed into an UNTYPED surface at run-time, as if it were created by &lt;newparam&gt;, using &lt;setparam&gt;. If there is a type mismatch between a &lt;setparam&gt; operation and what the run-time decides the type should be, the result is profile- and platform-specific behavior.
                    </xs:documentation>
                </xs:annotation>
            </xs:enumeration>
            <xs:enumeration value="1D"/>
            <xs:enumeration value="2D"/>
            <xs:enumeration value="3D"/>
            <xs:enumeration value="RECT"/>
            <xs:enumeration value="CUBE"/>
            <xs:enumeration value="DEPTH"/>
        </xs:restriction>
    </xs:simpleType>
    <xs:simpleType name="fx_surface_face_enum">
        <xs:restriction base="xs:string">
            <xs:enumeration value="POSITIVE_X"/>
            <xs:enumeration value="NEGATIVE_X"/>
            <xs:enumeration value="POSITIVE_Y"/>
            <xs:enumeration value="NEGATIVE_Y"/>
            <xs:enumeration value="POSITIVE_Z"/>
            <xs:enumeration value="NEGATIVE_Z"/>
        </xs:restriction>
    </xs:simpleType>
    <xs:simpleType name="fx_surface_format_hint_channels_enum">
        <xs:annotation>
            <xs:documentation>The per-texel layout of the format.  The length of the string indicate how many channels there are and the letter respresents the name of the channel.  There are typically 0 to 4 channels.</xs:documentation>
        </xs:annotation>
        <xs:restriction base="xs:string">
            <xs:enumeration value="RGB">
                <xs:annotation>
                    <xs:documentation>RGB color  map</xs:documentation>
                </xs:annotation>
            </xs:enumeration>
            <xs:enumeration value="RGBA">
                <xs:annotation>
                    <xs:documentation>RGB color + Alpha map often used for color + transparency or other things packed into channel A like specular power </xs:documentation>
                </xs:annotation>
            </xs:enumeration>
            <xs:enumeration value="L">
                <xs:annotation>
                    <xs:documentation>Luminance map often used for light mapping </xs:documentation>
                </xs:annotation>
            </xs:enumeration>
            <xs:enumeration value="LA">
                <xs:annotation>
                    <xs:documentation>Luminance+Alpha map often used for light mapping </xs:documentation>
                </xs:annotation>
            </xs:enumeration>
            <xs:enumeration value="D">
                <xs:annotation>
                    <xs:documentation>Depth map often used for displacement, parellax, relief, or shadow mapping </xs:documentation>
                </xs:annotation>
            </xs:enumeration>
            <xs:enumeration value="XYZ">
                <xs:annotation>
                    <xs:documentation>Typically used for normal maps or 3component displacement maps.</xs:documentation>
                </xs:annotation>
            </xs:enumeration>
            <xs:enumeration value="XYZW">
                <xs:annotation>
                    <xs:documentation>Typically used for normal maps where W is the depth for relief or parrallax mapping </xs:documentation>
                </xs:annotation>
            </xs:enumeration>
        </xs:restriction>
    </xs:simpleType>
    <xs:simpleType name="fx_surface_format_hint_precision_enum">
        <xs:annotation>
            <xs:documentation>Each channel of the texel has a precision.  Typically these are all linked together.  An exact format lay lower the precision of an individual channel but applying a higher precision by linking the channels together may still convey the same information.</xs:documentation>
        </xs:annotation>
        <xs:restriction base="xs:string">
            <xs:enumeration value="LOW">
                <xs:annotation>
                    <xs:documentation>For integers this typically represents 8 bits.  For floats typically 16 bits.</xs:documentation>
                </xs:annotation>
            </xs:enumeration>
            <xs:enumeration value="MID">
                <xs:annotation>
                    <xs:documentation>For integers this typically represents 8 to 24 bits.  For floats typically 16 to 32 bits.</xs:documentation>
                </xs:annotation>
            </xs:enumeration>
            <xs:enumeration value="HIGH">
                <xs:annotation>
                    <xs:documentation>For integers this typically represents 16 to 32 bits.  For floats typically 24 to 32 bits.</xs:documentation>
                </xs:annotation>
            </xs:enumeration>
        </xs:restriction>
    </xs:simpleType>
    <xs:simpleType name="fx_surface_format_hint_range_enum">
        <xs:annotation>
            <xs:documentation>Each channel represents a range of values. Some example ranges are signed or unsigned integers, or between between a clamped range such as 0.0f to 1.0f, or high dynamic range via floating point</xs:documentation>
        </xs:annotation>
        <xs:restriction base="xs:string">
            <xs:enumeration value="SNORM">
                <xs:annotation>
                    <xs:documentation>Format is representing a decimal value that remains within the -1 to 1 range. Implimentation could be integer-fixedpoint or floats.</xs:documentation>
                </xs:annotation>
            </xs:enumeration>
            <xs:enumeration value="UNORM">
                <xs:annotation>
                    <xs:documentation>Format is representing a decimal value that remains within the 0 to 1 range. Implimentation could be integer-fixedpoint or floats.</xs:documentation>
                </xs:annotation>
            </xs:enumeration>
            <xs:enumeration value="SINT">
                <xs:annotation>
                    <xs:documentation>Format is representing signed integer numbers.  (ex. 8bits = -128 to 127)</xs:documentation>
                </xs:annotation>
            </xs:enumeration>
            <xs:enumeration value="UINT">
                <xs:annotation>
                    <xs:documentation>Format is representing unsigned integer numbers.  (ex. 8bits = 0 to 255)</xs:documentation>
                </xs:annotation>
            </xs:enumeration>
            <xs:enumeration value="FLOAT">
                <xs:annotation>
                    <xs:documentation>Format should support full floating point ranges.  High precision is expected to be 32bit. Mid precision may be 16 to 32 bit.  Low precision is expected to be 16 bit.</xs:documentation>
                </xs:annotation>
            </xs:enumeration>
        </xs:restriction>
    </xs:simpleType>
    <xs:simpleType name="fx_surface_format_hint_option_enum">
        <xs:annotation>
            <xs:documentation>Additional hints about data relationships and other things to help the application pick the best format.</xs:documentation>
        </xs:annotation>
        <xs:restriction base="xs:string">
            <xs:enumeration value="SRGB_GAMMA">
                <xs:annotation>
                    <xs:documentation>colors are stored with respect to the sRGB 2.2 gamma curve rather than linear</xs:documentation>
                </xs:annotation>
            </xs:enumeration>
            <xs:enumeration value="NORMALIZED3">
                <xs:annotation>
                    <xs:documentation>the texel's XYZ/RGB should be normalized such as in a normal map.</xs:documentation>
                </xs:annotation>
            </xs:enumeration>
            <xs:enumeration value="NORMALIZED4">
                <xs:annotation>
                    <xs:documentation>the texel's XYZW/RGBA should be normalized such as in a normal map.</xs:documentation>
                </xs:annotation>
            </xs:enumeration>
            <xs:enumeration value="COMPRESSABLE">
                <xs:annotation>
                    <xs:documentation>The surface may use run-time compression.  Considering the best compression based on desired, channel, range, precision, and options </xs:documentation>
                </xs:annotation>
            </xs:enumeration>
        </xs:restriction>
    </xs:simpleType>
    <xs:complexType name="fx_surface_format_hint_common">
        <xs:annotation>
            <xs:documentation>If the exact format cannot be resolve via other methods then the format_hint will describe the important features of the format so that the application may select a compatable or close format</xs:documentation>
        </xs:annotation>
        <xs:sequence>
            <xs:element name="channels" type="fx_surface_format_hint_channels_enum">
                <xs:annotation>
                    <xs:documentation>The per-texel layout of the format.  The length of the string indicate how many channels there are and the letter respresents the name of the channel.  There are typically 0 to 4 channels.</xs:documentation>
                </xs:annotation>
            </xs:element>
            <xs:element name="range" type="fx_surface_format_hint_range_enum">
                <xs:annotation>
                    <xs:documentation>Each channel represents a range of values. Some example ranges are signed or unsigned integers, or between between a clamped range such as 0.0f to 1.0f, or high dynamic range via floating point</xs:documentation>
                </xs:annotation>
            </xs:element>
            <xs:element name="precision" type="fx_surface_format_hint_precision_enum" minOccurs="0">
                <xs:annotation>
                    <xs:documentation>Each channel of the texel has a precision.  Typically these are all linked together.  An exact format lay lower the precision of an individual channel but applying a higher precision by linking the channels together may still convey the same information.</xs:documentation>
                </xs:annotation>
            </xs:element>
            <xs:element name="option" type="fx_surface_format_hint_option_enum" minOccurs="0" maxOccurs="unbounded">
                <xs:annotation>
                    <xs:documentation>Additional hints about data relationships and other things to help the application pick the best format.</xs:documentation>
                </xs:annotation>
            </xs:element>
            <xs:element ref="extra" minOccurs="0" maxOccurs="unbounded"/>
        </xs:sequence>
    </xs:complexType>
    <xs:complexType name="fx_surface_init_planar_common">
        <xs:annotation>
            <xs:documentation>For 1D, 2D, RECT surface types</xs:documentation>
        </xs:annotation>
        <xs:choice>
            <xs:annotation>
                <xs:documentation>This choice exists for consistancy with other init types (volume and cube).  When other initialization methods are needed.</xs:documentation>
            </xs:annotation>
            <xs:element name="all">
                <xs:annotation>
                    <xs:documentation>Init the entire surface with one compound image such as DDS</xs:documentation>
                </xs:annotation>
                <xs:complexType>
                    <xs:attribute name="ref" type="xs:IDREF" use="required"/>
                </xs:complexType>
            </xs:element>
        </xs:choice>
    </xs:complexType>
    <xs:complexType name="fx_surface_init_volume_common">
        <xs:choice>
            <xs:element name="all">
                <xs:annotation>
                    <xs:documentation>Init the entire surface with one compound image such as DDS</xs:documentation>
                </xs:annotation>
                <xs:complexType>
                    <xs:attribute name="ref" type="xs:IDREF" use="required"/>
                </xs:complexType>
            </xs:element>
            <xs:element name="primary">
                <xs:annotation>
                    <xs:documentation>Init mip level 0 of the surface with one compound image such as DDS.  Use of this element expects that the surface has element mip_levels=0 or mipmap_generate.</xs:documentation>
                </xs:annotation>
                <xs:complexType>
                    <xs:attribute name="ref" type="xs:IDREF" use="required"/>
                </xs:complexType>
            </xs:element>
        </xs:choice>
    </xs:complexType>
    <xs:complexType name="fx_surface_init_cube_common">
        <xs:choice>
            <xs:element name="all">
                <xs:annotation>
                    <xs:documentation>Init the entire surface with one compound image such as DDS</xs:documentation>
                </xs:annotation>
                <xs:complexType>
                    <xs:attribute name="ref" type="xs:IDREF" use="required"/>
                </xs:complexType>
            </xs:element>
            <xs:element name="primary">
                <xs:annotation>
                    <xs:documentation>Init all primary mip level 0 subsurfaces with one compound image such as DDS.  Use of this element expects that the surface has element mip_levels=0 or mipmap_generate.</xs:documentation>
                </xs:annotation>
                <xs:complexType>
                    <xs:sequence minOccurs="0">
                        <xs:annotation>
                            <xs:documentation>This sequence exists to allow the order elements to be optional but require that if they exist there must be 6 of them.</xs:documentation>
                        </xs:annotation>
                        <xs:element name="order" type="fx_surface_face_enum" minOccurs="6" maxOccurs="6">
                            <xs:annotation>
                                <xs:documentation>If the image dues not natively describe the face ordering then this series of order elements will describe which face the index belongs too</xs:documentation>
                            </xs:annotation>
                        </xs:element>
                    </xs:sequence>
                    <xs:attribute name="ref" type="xs:IDREF" use="required"/>
                </xs:complexType>
            </xs:element>
            <xs:element name="face" minOccurs="6" maxOccurs="6">
                <xs:annotation>
                    <xs:documentation>Init each face mipchain with one compound image such as DDS</xs:documentation>
                </xs:annotation>
                <xs:complexType>
                    <xs:attribute name="ref" type="xs:IDREF" use="required"/>
                </xs:complexType>
            </xs:element>
        </xs:choice>
    </xs:complexType>
    <xs:complexType name="fx_surface_init_from_common">
        <xs:annotation>
            <xs:documentation>
                This element is an IDREF which specifies the image to use to initialize a specific mip of a 1D or 2D surface, 3D slice, or Cube face.
            </xs:documentation>
        </xs:annotation>
        <xs:simpleContent>
            <xs:extension base="xs:IDREF">
                <xs:attribute name="mip" type="xs:unsignedInt" default="0"/>
                <xs:attribute name="slice" type="xs:unsignedInt" default="0"/>
                <xs:attribute name="face" type="fx_surface_face_enum" default="POSITIVE_X"/>
            </xs:extension>
        </xs:simpleContent>
    </xs:complexType>
    <xs:group name="fx_surface_init_common">
        <xs:annotation>
            <xs:documentation>The common set of initalization options for surfaces.  Choose which is appropriate for your surface based on type and other characteristics. described by the annotation docs on the child elements.</xs:documentation>
        </xs:annotation>
        <xs:choice>
            <xs:element name="init_as_null">
                <xs:annotation>
                    <xs:documentation>This surface is intended to be initialized later externally by a "setparam" element.  If it is used before being initialized there is profile and platform specific behavior.  Most elements on the surface element containing this will be ignored including mip_levels, mipmap_generate, size, viewport_ratio, and format.</xs:documentation>
                </xs:annotation>
            </xs:element>
            <xs:element name="init_as_target">
                <xs:annotation>
                    <xs:documentation>Init as a target for depth, stencil, or color.  It does not need image data. Surface should not have mipmap_generate when using this.</xs:documentation>
                </xs:annotation>
            </xs:element>
            <xs:element name="init_cube" type="fx_surface_init_cube_common">
                <xs:annotation>
                    <xs:documentation>Init a CUBE from a compound image such as DDS</xs:documentation>
                </xs:annotation>
            </xs:element>
            <xs:element name="init_volume" type="fx_surface_init_volume_common">
                <xs:annotation>
                    <xs:documentation>Init a 3D from a compound image such as DDS</xs:documentation>
                </xs:annotation>
            </xs:element>
            <xs:element name="init_planar" type="fx_surface_init_planar_common">
                <xs:annotation>
                    <xs:documentation>Init a 1D,2D,RECT,DEPTH from a compound image such as DDS</xs:documentation>
                </xs:annotation>
            </xs:element>
            <xs:element name="init_from" type="fx_surface_init_from_common" maxOccurs="unbounded">
                <xs:annotation>
                    <xs:documentation>Initialize the surface one sub-surface at a time by specifying combinations of mip, face, and slice which make sense for a particular surface type.  Each sub-surface is initialized by a common 2D image, not a complex compound image such as DDS. If not all subsurfaces are initialized, it is invalid and will result in profile and platform specific behavior unless mipmap_generate is responsible for initializing the remainder of the sub-surfaces</xs:documentation>
                </xs:annotation>
            </xs:element>
        </xs:choice>
    </xs:group>
    <xs:complexType name="fx_surface_common">
        <xs:annotation>
            <xs:documentation>
            The fx_surface_common type is used to declare a resource that can be used both as the source for texture samples and as the target of a rendering pass.
            </xs:documentation>
        </xs:annotation>
        <xs:sequence>
            <xs:group ref="fx_surface_init_common" minOccurs="0">
                <xs:annotation>
                    <xs:documentation>The common set of initalization options for surfaces.  Choose which is appropriate for your surface based on the type attribute and other characteristics described by the annotation docs on the choiced child elements of this type.</xs:documentation>
                </xs:annotation>
            </xs:group>
            <xs:element name="format" type="xs:token" minOccurs="0">
                <xs:annotation>
                    <xs:documentation>Contains a string representing the profile and platform specific texel format that the author would like this surface to use.  If this element is not specified then the application will use a common format R8G8B8A8 with linear color gradient, not  sRGB.</xs:documentation>
                </xs:annotation>
            </xs:element>
            <xs:element name="format_hint" type="fx_surface_format_hint_common" minOccurs="0">
                <xs:annotation>
                    <xs:documentation>If the exact format cannot be resolved via the "format" element then the format_hint will describe the important features of the format so that the application may select a compatable or close format</xs:documentation>
                </xs:annotation>
            </xs:element>
            <xs:choice minOccurs="0">
                <xs:element name="size" type="int3" default="0 0 0">
                    <xs:annotation>
                        <xs:documentation>The surface should be sized to these exact dimensions</xs:documentation>
                    </xs:annotation>
                </xs:element>
                <xs:element name="viewport_ratio" type="float2" default="1 1">
                    <xs:annotation>
                        <xs:documentation>The surface should be sized to a dimension based on this ratio of the viewport's dimensions in pixels</xs:documentation>
                    </xs:annotation>
                </xs:element>
            </xs:choice>
            <xs:element name="mip_levels" type="xs:unsignedInt" default="0" minOccurs="0">
                <xs:annotation>
                    <xs:documentation>the surface should contain the following number of MIP levels.  If this element is not present it is assumed that all miplevels exist until a dimension becomes 1 texel.  To create a surface that has only one level of mip maps (mip=0) set this to 1.  If the value is 0 the result is the same as if mip_levels was unspecified, all possible mip_levels will exist.</xs:documentation>
                </xs:annotation>
            </xs:element>
            <xs:element name="mipmap_generate" type="xs:boolean" minOccurs="0">
                <xs:annotation>
                    <xs:documentation>By default it is assumed that mipmaps are supplied by the author so, if not all subsurfaces are initialized, it is invalid and will result in profile and platform specific behavior unless mipmap_generate is responsible for initializing the remainder of the sub-surfaces</xs:documentation>
                </xs:annotation>
            </xs:element>
            <xs:element ref="extra" minOccurs="0" maxOccurs="unbounded"/>
        </xs:sequence>
        <xs:attribute name="type" type="fx_surface_type_enum" use="required">
            <xs:annotation>
                <xs:documentation>Specifying the type of a surface is mandatory though the type may be "UNTYPED".  When a surface is typed as UNTYPED, it is said to be temporarily untyped and instead will be typed later by the context it is used in such as which samplers reference it in that are used in a particular technique or pass.   If there is a type mismatch between what is set into it later and what the runtime decides the type should be the result in profile and platform specific behavior.</xs:documentation>
            </xs:annotation>
        </xs:attribute>
    </xs:complexType>
    <xs:simpleType name="fx_sampler_wrap_common">
        <xs:restriction base="xs:NMTOKEN">
            <xs:enumeration value="NONE"/>
            <xs:enumeration value="WRAP"/>
            <xs:enumeration value="MIRROR"/>
            <xs:enumeration value="CLAMP"/>
            <xs:enumeration value="BORDER"/>
        </xs:restriction>
    </xs:simpleType>
    <xs:simpleType name="fx_sampler_filter_common">
        <xs:restriction base="xs:NMTOKEN">
            <xs:enumeration value="NONE"/>
            <xs:enumeration value="NEAREST"/>
            <xs:enumeration value="LINEAR"/>
            <xs:enumeration value="NEAREST_MIPMAP_NEAREST"/>
            <xs:enumeration value="LINEAR_MIPMAP_NEAREST"/>
            <xs:enumeration value="NEAREST_MIPMAP_LINEAR"/>
            <xs:enumeration value="LINEAR_MIPMAP_LINEAR"/>
        </xs:restriction>
    </xs:simpleType>
    <xs:complexType name="fx_sampler1D_common">
        <xs:annotation>
            <xs:documentation>
            A one-dimensional texture sampler.
            </xs:documentation>
        </xs:annotation>
        <xs:sequence>
            <xs:element name="source" type="xs:NCName"/>
            <xs:element name="wrap_s" type="fx_sampler_wrap_common" default="WRAP" minOccurs="0"/>
            <xs:element name="minfilter" type="fx_sampler_filter_common" default="NONE" minOccurs="0"/>
            <xs:element name="magfilter" type="fx_sampler_filter_common" default="NONE" minOccurs="0"/>
            <xs:element name="mipfilter" type="fx_sampler_filter_common" default="NONE" minOccurs="0"/>
            <xs:element name="border_color" type="fx_color_common" minOccurs="0"/>
            <xs:element name="mipmap_maxlevel" type="xs:unsignedByte" default="0" minOccurs="0"/>
            <xs:element name="mipmap_bias" type="xs:float" default="0.0" minOccurs="0"/>
            <xs:element ref="extra" minOccurs="0" maxOccurs="unbounded"/>
        </xs:sequence>
    </xs:complexType>
    <xs:complexType name="fx_sampler2D_common">
        <xs:annotation>
            <xs:documentation>
            A two-dimensional texture sampler.
            </xs:documentation>
        </xs:annotation>
        <xs:sequence>
            <xs:element name="source" type="xs:NCName"/>
            <xs:element name="wrap_s" type="fx_sampler_wrap_common" default="WRAP" minOccurs="0"/>
            <xs:element name="wrap_t" type="fx_sampler_wrap_common" default="WRAP" minOccurs="0"/>
            <xs:element name="minfilter" type="fx_sampler_filter_common" default="NONE" minOccurs="0"/>
            <xs:element name="magfilter" type="fx_sampler_filter_common" default="NONE" minOccurs="0"/>
            <xs:element name="mipfilter" type="fx_sampler_filter_common" default="NONE" minOccurs="0"/>
            <xs:element name="border_color" type="fx_color_common" minOccurs="0"/>
            <xs:element name="mipmap_maxlevel" type="xs:unsignedByte" default="255" minOccurs="0"/>
            <xs:element name="mipmap_bias" type="xs:float" default="0.0" minOccurs="0"/>
            <xs:element ref="extra" minOccurs="0" maxOccurs="unbounded"/>
        </xs:sequence>
    </xs:complexType>
    <xs:complexType name="fx_sampler3D_common">
        <xs:annotation>
            <xs:documentation>
            A three-dimensional texture sampler.
            </xs:documentation>
        </xs:annotation>
        <xs:sequence>
            <xs:element name="source" type="xs:NCName"/>
            <xs:element name="wrap_s" type="fx_sampler_wrap_common" default="WRAP" minOccurs="0"/>
            <xs:element name="wrap_t" type="fx_sampler_wrap_common" default="WRAP" minOccurs="0"/>
            <xs:element name="wrap_p" type="fx_sampler_wrap_common" default="WRAP" minOccurs="0"/>
            <xs:element name="minfilter" type="fx_sampler_filter_common" default="NONE" minOccurs="0"/>
            <xs:element name="magfilter" type="fx_sampler_filter_common" default="NONE" minOccurs="0"/>
            <xs:element name="mipfilter" type="fx_sampler_filter_common" default="NONE" minOccurs="0"/>
            <xs:element name="border_color" type="fx_color_common" minOccurs="0"/>
            <xs:element name="mipmap_maxlevel" type="xs:unsignedByte" default="255" minOccurs="0"/>
            <xs:element name="mipmap_bias" type="xs:float" default="0.0" minOccurs="0"/>
            <xs:element ref="extra" minOccurs="0" maxOccurs="unbounded"/>
        </xs:sequence>
    </xs:complexType>
    <xs:complexType name="fx_samplerCUBE_common">
        <xs:annotation>
            <xs:documentation>
            A texture sampler for cube maps.
            </xs:documentation>
        </xs:annotation>
        <xs:sequence>
            <xs:element name="source" type="xs:NCName"/>
            <xs:element name="wrap_s" type="fx_sampler_wrap_common" default="WRAP" minOccurs="0"/>
            <xs:element name="wrap_t" type="fx_sampler_wrap_common" default="WRAP" minOccurs="0"/>
            <xs:element name="wrap_p" type="fx_sampler_wrap_common" default="WRAP" minOccurs="0"/>
            <xs:element name="minfilter" type="fx_sampler_filter_common" default="NONE" minOccurs="0"/>
            <xs:element name="magfilter" type="fx_sampler_filter_common" default="NONE" minOccurs="0"/>
            <xs:element name="mipfilter" type="fx_sampler_filter_common" default="NONE" minOccurs="0"/>
            <xs:element name="border_color" type="fx_color_common" minOccurs="0"/>
            <xs:element name="mipmap_maxlevel" type="xs:unsignedByte" default="255" minOccurs="0"/>
            <xs:element name="mipmap_bias" type="xs:float" default="0.0" minOccurs="0"/>
            <xs:element ref="extra" minOccurs="0" maxOccurs="unbounded"/>
        </xs:sequence>
    </xs:complexType>
    <xs:complexType name="fx_samplerRECT_common">
        <xs:annotation>
            <xs:documentation>
            A two-dimensional texture sampler.
            </xs:documentation>
        </xs:annotation>
        <xs:sequence>
            <xs:element name="source" type="xs:NCName"/>
            <xs:element name="wrap_s" type="fx_sampler_wrap_common" default="WRAP" minOccurs="0"/>
            <xs:element name="wrap_t" type="fx_sampler_wrap_common" default="WRAP" minOccurs="0"/>
            <xs:element name="minfilter" type="fx_sampler_filter_common" default="NONE" minOccurs="0"/>
            <xs:element name="magfilter" type="fx_sampler_filter_common" default="NONE" minOccurs="0"/>
            <xs:element name="mipfilter" type="fx_sampler_filter_common" default="NONE" minOccurs="0"/>
            <xs:element name="border_color" type="fx_color_common" minOccurs="0"/>
            <xs:element name="mipmap_maxlevel" type="xs:unsignedByte" default="255" minOccurs="0"/>
            <xs:element name="mipmap_bias" type="xs:float" default="0.0" minOccurs="0"/>
            <xs:element ref="extra" minOccurs="0" maxOccurs="unbounded"/>
        </xs:sequence>
    </xs:complexType>
    <xs:complexType name="fx_samplerDEPTH_common">
        <xs:annotation>
            <xs:documentation>
            A texture sampler for depth maps.
            </xs:documentation>
        </xs:annotation>
        <xs:sequence>
            <xs:element name="source" type="xs:NCName"/>
            <xs:element name="wrap_s" type="fx_sampler_wrap_common" default="WRAP" minOccurs="0"/>
            <xs:element name="wrap_t" type="fx_sampler_wrap_common" default="WRAP" minOccurs="0"/>
            <xs:element name="minfilter" type="fx_sampler_filter_common" default="NONE" minOccurs="0"/>
            <xs:element name="magfilter" type="fx_sampler_filter_common" default="NONE" minOccurs="0"/>
            <xs:element ref="extra" minOccurs="0" maxOccurs="unbounded"/>
        </xs:sequence>
    </xs:complexType>
    <xs:group name="fx_annotate_type_common">
        <xs:annotation>
            <xs:documentation>
            A group that specifies the allowable types for an annotation.
            </xs:documentation>
        </xs:annotation>
        <xs:choice>
            <xs:element name="bool" type="bool"/>
            <xs:element name="bool2" type="bool2"/>
            <xs:element name="bool3" type="bool3"/>
            <xs:element name="bool4" type="bool4"/>
            <xs:element name="int" type="int"/>
            <xs:element name="int2" type="int2"/>
            <xs:element name="int3" type="int3"/>
            <xs:element name="int4" type="int4"/>
            <xs:element name="float" type="float"/>
            <xs:element name="float2" type="float2"/>
            <xs:element name="float3" type="float3"/>
            <xs:element name="float4" type="float4"/>
            <xs:element name="float2x2" type="float2x2"/>
            <xs:element name="float3x3" type="float3x3"/>
            <xs:element name="float4x4" type="float4x4"/>
            <xs:element name="string" type="xs:string"/>
        </xs:choice>
    </xs:group>
    <xs:group name="fx_basic_type_common">
        <xs:annotation>
            <xs:documentation>
            A group that specifies the allowable types for effect scoped parameters.
            </xs:documentation>
        </xs:annotation>
        <xs:choice>
            <xs:element name="bool" type="bool"/>
            <xs:element name="bool2" type="bool2"/>
            <xs:element name="bool3" type="bool3"/>
            <xs:element name="bool4" type="bool4"/>
            <xs:element name="int" type="int"/>
            <xs:element name="int2" type="int2"/>
            <xs:element name="int3" type="int3"/>
            <xs:element name="int4" type="int4"/>
            <xs:element name="float" type="float"/>
            <xs:element name="float2" type="float2"/>
            <xs:element name="float3" type="float3"/>
            <xs:element name="float4" type="float4"/>
            <xs:element name="float1x1" type="float"/>
            <xs:element name="float1x2" type="float2"/>
            <xs:element name="float1x3" type="float3"/>
            <xs:element name="float1x4" type="float4"/>
            <xs:element name="float2x1" type="float2"/>
            <xs:element name="float2x2" type="float2x2"/>
            <xs:element name="float2x3" type="float2x3"/>
            <xs:element name="float2x4" type="float2x4"/>
            <xs:element name="float3x1" type="float3"/>
            <xs:element name="float3x2" type="float3x2"/>
            <xs:element name="float3x3" type="float3x3"/>
            <xs:element name="float3x4" type="float3x4"/>
            <xs:element name="float4x1" type="float4"/>
            <xs:element name="float4x2" type="float4x2"/>
            <xs:element name="float4x3" type="float4x3"/>
            <xs:element name="float4x4" type="float4x4"/>
            <xs:element name="surface" type="fx_surface_common"/>
            <xs:element name="sampler1D" type="fx_sampler1D_common"/>
            <xs:element name="sampler2D" type="fx_sampler2D_common"/>
            <xs:element name="sampler3D" type="fx_sampler3D_common"/>
            <xs:element name="samplerCUBE" type="fx_samplerCUBE_common"/>
            <xs:element name="samplerRECT" type="fx_samplerRECT_common"/>
            <xs:element name="samplerDEPTH" type="fx_samplerDEPTH_common"/>
            <xs:element name="enum" type="xs:string"/>
        </xs:choice>
    </xs:group>
    <xs:simpleType name="fx_modifier_enum_common">
        <xs:restriction base="xs:NMTOKEN">
            <xs:enumeration value="CONST"/>
            <xs:enumeration value="UNIFORM"/>
            <xs:enumeration value="VARYING"/>
            <xs:enumeration value="STATIC"/>
            <xs:enumeration value="VOLATILE"/>
            <xs:enumeration value="EXTERN"/>
            <xs:enumeration value="SHARED"/>
        </xs:restriction>
    </xs:simpleType>
    <xs:complexType name="fx_colortarget_common">
        <xs:simpleContent>
            <xs:extension base="xs:NCName">
                <xs:attribute name="index" type="xs:nonNegativeInteger" use="optional" default="0"/>
                <xs:attribute name="face" type="fx_surface_face_enum" use="optional" default="POSITIVE_X"/>
                <xs:attribute name="mip" type="xs:nonNegativeInteger" use="optional" default="0"/>
                <xs:attribute name="slice" type="xs:nonNegativeInteger" use="optional" default="0"/>
            </xs:extension>
        </xs:simpleContent>
    </xs:complexType>
    <xs:complexType name="fx_depthtarget_common">
        <xs:simpleContent>
            <xs:extension base="xs:NCName">
                <xs:attribute name="index" type="xs:nonNegativeInteger" use="optional" default="0"/>
                <xs:attribute name="face" type="fx_surface_face_enum" use="optional" default="POSITIVE_X"/>
                <xs:attribute name="mip" type="xs:nonNegativeInteger" use="optional" default="0"/>
                <xs:attribute name="slice" type="xs:nonNegativeInteger" use="optional" default="0"/>
            </xs:extension>
        </xs:simpleContent>
    </xs:complexType>
    <xs:complexType name="fx_stenciltarget_common">
        <xs:simpleContent>
            <xs:extension base="xs:NCName">
                <xs:attribute name="index" type="xs:nonNegativeInteger" use="optional" default="0"/>
                <xs:attribute name="face" type="fx_surface_face_enum" use="optional" default="POSITIVE_X"/>
                <xs:attribute name="mip" type="xs:nonNegativeInteger" use="optional" default="0"/>
                <xs:attribute name="slice" type="xs:nonNegativeInteger" use="optional" default="0"/>
            </xs:extension>
        </xs:simpleContent>
    </xs:complexType>
    <xs:complexType name="fx_clearcolor_common">
        <xs:simpleContent>
            <xs:extension base="fx_color_common">
                <xs:attribute name="index" type="xs:nonNegativeInteger" use="optional" default="0"/>
            </xs:extension>
        </xs:simpleContent>
    </xs:complexType>
    <xs:complexType name="fx_cleardepth_common">
        <xs:simpleContent>
            <xs:extension base="float">
                <xs:attribute name="index" type="xs:nonNegativeInteger" use="optional" default="0"/>
            </xs:extension>
        </xs:simpleContent>
    </xs:complexType>
    <xs:complexType name="fx_clearstencil_common">
        <xs:simpleContent>
            <xs:extension base="xs:byte">
                <xs:attribute name="index" type="xs:nonNegativeInteger" use="optional" default="0"/>
            </xs:extension>
        </xs:simpleContent>
    </xs:complexType>
    <xs:simpleType name="fx_draw_common">
        <xs:restriction base="xs:string"/>
    </xs:simpleType>
    <xs:simpleType name="fx_pipeline_stage_common">
        <xs:restriction base="xs:string">
            <xs:enumeration value="VERTEXPROGRAM"/>
            <xs:enumeration value="FRAGMENTPROGRAM"/>
            <xs:enumeration value="VERTEXSHADER"/>
            <xs:enumeration value="PIXELSHADER"/>
        </xs:restriction>
    </xs:simpleType>
    <!-- =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=- -->
    <!-- COLLADA FX elements in common scope    -->
    <!-- =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=- -->
    <xs:complexType name="fx_annotate_common">
        <xs:sequence>
            <xs:group ref="fx_annotate_type_common"/>
        </xs:sequence>
        <xs:attribute name="name" type="xs:NCName" use="required"/>
    </xs:complexType>
    <xs:complexType name="fx_include_common">
        <xs:annotation>
            <xs:documentation>
            The include element is used to import source code or precompiled binary shaders into the FX Runtime by referencing an external resource.
            </xs:documentation>
        </xs:annotation>
        <xs:attribute name="sid" type="xs:NCName" use="required">
            <xs:annotation>
                <xs:documentation>
                    The sid attribute is a text string value containing the sub-identifier of this element.
                    This value must be unique within the scope of the parent element. Optional attribute.
                </xs:documentation>
            </xs:annotation>
        </xs:attribute>
        <xs:attribute name="url" type="xs:anyURI" use="required">
            <xs:annotation>
                <xs:documentation>
                    The url attribute refers to resource.  This may refer to a local resource using a relative URL
                    fragment identifier that begins with the “#” character. The url attribute may refer to an external
                    resource using an absolute or relative URL.
                </xs:documentation>
            </xs:annotation>
        </xs:attribute>
    </xs:complexType>
    <xs:complexType name="fx_newparam_common">
        <xs:annotation>
            <xs:documentation>
            This element creates a new, named param object in the FX Runtime, assigns it a type, an initial value, and additional attributes at declaration time.
            </xs:documentation>
        </xs:annotation>
        <xs:sequence>
            <xs:element name="annotate" type="fx_annotate_common" minOccurs="0" maxOccurs="unbounded">
                <xs:annotation>
                    <xs:documentation>
                    The annotate element allows you to specify an annotation for this new param.
                    </xs:documentation>
                </xs:annotation>
            </xs:element>
            <xs:element name="semantic" type="xs:NCName" minOccurs="0">
                <xs:annotation>
                    <xs:documentation>
                    The semantic element allows you to specify a semantic for this new param.
                    </xs:documentation>
                </xs:annotation>
            </xs:element>
            <xs:element name="modifier" type="fx_modifier_enum_common" minOccurs="0">
                <xs:annotation>
                    <xs:documentation>
                    The modifier element allows you to specify a modifier for this new param.
                    </xs:documentation>
                </xs:annotation>
            </xs:element>
            <xs:group ref="fx_basic_type_common"/>
        </xs:sequence>
        <xs:attribute name="sid" type="xs:NCName" use="required">
            <xs:annotation>
                <xs:documentation>
                The sid attribute is a text string value containing the sub-identifier of this element.
                This value must be unique within the scope of the parent element. Optional attribute.
                </xs:documentation>
            </xs:annotation>
        </xs:attribute>
    </xs:complexType>
    <!-- =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-= -->
    <!-- COLLADA FX types in profile scope   -->
    <!-- =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-= -->
    <xs:complexType name="fx_code_profile">
        <xs:annotation>
            <xs:documentation>
            The fx_code_profile type allows you to specify an inline block of source code.
            </xs:documentation>
        </xs:annotation>
        <xs:simpleContent>
            <xs:extension base="xs:string">
                <xs:attribute name="sid" type="xs:NCName" use="optional">
                    <xs:annotation>
                        <xs:documentation>
                        The sid attribute is a text string value containing the sub-identifier of this element.
                        This value must be unique within the scope of the parent element. Optional attribute.
                        </xs:documentation>
                    </xs:annotation>
                </xs:attribute>
            </xs:extension>
        </xs:simpleContent>
    </xs:complexType>
    <!-- =-=-=-=-=-=-=-=-=-=-=-=-=-=-= -->
    <!-- COLLADA FX effect elements    -->
    <!-- =-=-=-=-=-=-=-=-=-=-=-=-=-=-= -->
    <xs:element name="fx_profile_abstract" abstract="true">
        <xs:annotation>
            <xs:documentation>
            The fx_profile_abstract element is only used as a substitution group hook for COLLADA FX profiles.
            </xs:documentation>
        </xs:annotation>
    </xs:element>
    <xs:element name="effect">
        <xs:annotation>
            <xs:documentation>
            A self contained description of a shader effect.
            </xs:documentation>
        </xs:annotation>
        <xs:complexType>
            <xs:sequence>
                <xs:element ref="asset" minOccurs="0">
                    <xs:annotation>
                        <xs:documentation>
                        The effect element may contain an asset element.
                        </xs:documentation>
                    </xs:annotation>
                </xs:element>
                <xs:element name="annotate" type="fx_annotate_common" minOccurs="0" maxOccurs="unbounded">
                    <xs:annotation>
                        <xs:documentation>
                        The annotate element allows you to specify an annotation on this effect.
                        </xs:documentation>
                    </xs:annotation>
                </xs:element>
                <xs:element ref="image" minOccurs="0" maxOccurs="unbounded">
                    <xs:annotation>
                        <xs:documentation>
                        The image element allows you to create image resources which can be shared by multipe profiles.
                        </xs:documentation>
                    </xs:annotation>
                </xs:element>
                <xs:element name="newparam" type="fx_newparam_common" minOccurs="0" maxOccurs="unbounded">
                    <xs:annotation>
                        <xs:documentation>
                        The newparam element allows you to create new effect parameters which can be shared by multipe profiles.
                        </xs:documentation>
                    </xs:annotation>
                </xs:element>
                <xs:element ref="fx_profile_abstract" maxOccurs="unbounded">
                    <xs:annotation>
                        <xs:documentation>
                        This is the substituion group hook which allows you to swap in other COLLADA FX profiles.
                        </xs:documentation>
                    </xs:annotation>
                </xs:element>
                <xs:element ref="extra" minOccurs="0" maxOccurs="unbounded">
                    <xs:annotation>
                        <xs:documentation>
                        The extra element may appear any number of times.
                        </xs:documentation>
                    </xs:annotation>
                </xs:element>
            </xs:sequence>
            <xs:attribute name="id" type="xs:ID" use="required">
                <xs:annotation>
                    <xs:documentation>
                    The id attribute is a text string containing the unique identifier of this element.
                    This value must be unique within the instance document. Optional attribute.
                    </xs:documentation>
                </xs:annotation>
            </xs:attribute>
            <xs:attribute name="name" type="xs:NCName">
                <xs:annotation>
                    <xs:documentation>
                    The name attribute is the text string name of this element. Optional attribute.
                    </xs:documentation>
                </xs:annotation>
            </xs:attribute>
        </xs:complexType>
    </xs:element>
    <!-- =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-= -->
    <!-- COLLADA FX GLSL elements                  -->
    <!-- =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-= -->
    <xs:simpleType name="GL_MAX_LIGHTS_index">
        <xs:restriction base="xs:nonNegativeInteger">
            <xs:minInclusive value="0"/>
        </xs:restriction>
    </xs:simpleType>
    <xs:simpleType name="GL_MAX_CLIP_PLANES_index">
        <xs:restriction base="xs:nonNegativeInteger">
            <xs:minInclusive value="0"/>
        </xs:restriction>
    </xs:simpleType>
    <xs:simpleType name="GL_MAX_TEXTURE_IMAGE_UNITS_index">
        <xs:restriction base="xs:nonNegativeInteger">
            <xs:minInclusive value="0"/>
        </xs:restriction>
    </xs:simpleType>
    <xs:complexType name="gl_sampler1D">
        <xs:annotation>
            <xs:documentation>
            A one-dimensional texture sampler for the GLSL profile.
            </xs:documentation>
        </xs:annotation>
        <xs:complexContent>
            <xs:extension base="fx_sampler1D_common"/>
        </xs:complexContent>
    </xs:complexType>
    <xs:complexType name="gl_sampler2D">
        <xs:annotation>
            <xs:documentation>
            A two-dimensional texture sampler for the GLSL profile.
            </xs:documentation>
        </xs:annotation>
        <xs:complexContent>
            <xs:extension base="fx_sampler2D_common"/>
        </xs:complexContent>
    </xs:complexType>
    <xs:complexType name="gl_sampler3D">
        <xs:annotation>
            <xs:documentation>
            A three-dimensional texture sampler for the GLSL profile.
            </xs:documentation>
        </xs:annotation>
        <xs:complexContent>
            <xs:extension base="fx_sampler3D_common"/>
        </xs:complexContent>
    </xs:complexType>
    <xs:complexType name="gl_samplerCUBE">
        <xs:annotation>
            <xs:documentation>
            A cube map texture sampler for the GLSL profile.
            </xs:documentation>
        </xs:annotation>
        <xs:complexContent>
            <xs:extension base="fx_samplerCUBE_common"/>
        </xs:complexContent>
    </xs:complexType>
    <xs:complexType name="gl_samplerRECT">
        <xs:annotation>
            <xs:documentation>
            A two-dimensional texture sampler for the GLSL profile.
            </xs:documentation>
        </xs:annotation>
        <xs:complexContent>
            <xs:extension base="fx_samplerRECT_common"/>
        </xs:complexContent>
    </xs:complexType>
    <xs:complexType name="gl_samplerDEPTH">
        <xs:annotation>
            <xs:documentation>
            A depth texture sampler for the GLSL profile.
            </xs:documentation>
        </xs:annotation>
        <xs:complexContent>
            <xs:extension base="fx_samplerDEPTH_common"/>
        </xs:complexContent>
    </xs:complexType>
    <xs:simpleType name="gl_blend_type">
        <xs:restriction base="xs:string">
            <xs:enumeration value="ZERO">
                <xs:annotation>
                    <xs:appinfo>value=0x0</xs:appinfo>
                </xs:annotation>
            </xs:enumeration>
            <xs:enumeration value="ONE">
                <xs:annotation>
                    <xs:appinfo>value=0x1</xs:appinfo>
                </xs:annotation>
            </xs:enumeration>
            <xs:enumeration value="SRC_COLOR">
                <xs:annotation>
                    <xs:appinfo>value=0x0300</xs:appinfo>
                </xs:annotation>
            </xs:enumeration>
            <xs:enumeration value="ONE_MINUS_SRC_COLOR">
                <xs:annotation>
                    <xs:appinfo>value=0x0301</xs:appinfo>
                </xs:annotation>
            </xs:enumeration>
            <xs:enumeration value="DEST_COLOR">
                <xs:annotation>
                    <xs:appinfo>value=0x0306</xs:appinfo>
                </xs:annotation>
            </xs:enumeration>
            <xs:enumeration value="ONE_MINUS_DEST_COLOR">
                <xs:annotation>
                    <xs:appinfo>value=0x0307</xs:appinfo>
                </xs:annotation>
            </xs:enumeration>
            <xs:enumeration value="SRC_ALPHA">
                <xs:annotation>
                    <xs:appinfo>value=0x0302</xs:appinfo>
                </xs:annotation>
            </xs:enumeration>
            <xs:enumeration value="ONE_MINUS_SRC_ALPHA">
                <xs:annotation>
                    <xs:appinfo>value=0x0303</xs:appinfo>
                </xs:annotation>
            </xs:enumeration>
            <xs:enumeration value="DST_ALPHA">
                <xs:annotation>
                    <xs:appinfo>value=0x0304</xs:appinfo>
                </xs:annotation>
            </xs:enumeration>
            <xs:enumeration value="ONE_MINUS_DST_ALPHA">
                <xs:annotation>
                    <xs:appinfo>value=0x0305</xs:appinfo>
                </xs:annotation>
            </xs:enumeration>
            <xs:enumeration value="CONSTANT_COLOR">
                <xs:annotation>
                    <xs:appinfo>value=0x8001</xs:appinfo>
                </xs:annotation>
            </xs:enumeration>
            <xs:enumeration value="ONE_MINUS_CONSTANT_COLOR">
                <xs:annotation>
                    <xs:appinfo>value=0x8002</xs:appinfo>
                </xs:annotation>
            </xs:enumeration>
            <xs:enumeration value="CONSTANT_ALPHA">
                <xs:annotation>
                    <xs:appinfo>value=0x8003</xs:appinfo>
                </xs:annotation>
            </xs:enumeration>
            <xs:enumeration value="ONE_MINUS_CONSTANT_ALPHA">
                <xs:annotation>
                    <xs:appinfo>value=0x8004</xs:appinfo>
                </xs:annotation>
            </xs:enumeration>
            <xs:enumeration value="SRC_ALPHA_SATURATE">
                <xs:annotation>
                    <xs:appinfo>value=0x0308</xs:appinfo>
                </xs:annotation>
            </xs:enumeration>
        </xs:restriction>
    </xs:simpleType>
    <xs:simpleType name="gl_face_type">
        <xs:restriction base="xs:string">
            <xs:enumeration value="FRONT">
                <xs:annotation>
                    <xs:appinfo>value=0x0404</xs:appinfo>
                </xs:annotation>
            </xs:enumeration>
            <xs:enumeration value="BACK">
                <xs:annotation>
                    <xs:appinfo>value=0x0405</xs:appinfo>
                </xs:annotation>
            </xs:enumeration>
            <xs:enumeration value="FRONT_AND_BACK">
                <xs:annotation>
                    <xs:appinfo>value=0x0408</xs:appinfo>
                </xs:annotation>
            </xs:enumeration>
        </xs:restriction>
    </xs:simpleType>
    <xs:simpleType name="gl_blend_equation_type">
        <xs:restriction base="xs:string">
            <xs:enumeration value="FUNC_ADD">
                <xs:annotation>
                    <xs:appinfo>value=0x8006</xs:appinfo>
                </xs:annotation>
            </xs:enumeration>
            <xs:enumeration value="FUNC_SUBTRACT">
                <xs:annotation>
                    <xs:appinfo>value=0x800A</xs:appinfo>
                </xs:annotation>
            </xs:enumeration>
            <xs:enumeration value="FUNC_REVERSE_SUBTRACT">
                <xs:annotation>
                    <xs:appinfo>value=0x800B</xs:appinfo>
                </xs:annotation>
            </xs:enumeration>
            <xs:enumeration value="MIN">
                <xs:annotation>
                    <xs:appinfo>value=0x8007</xs:appinfo>
                </xs:annotation>
            </xs:enumeration>
            <xs:enumeration value="MAX">
                <xs:annotation>
                    <xs:appinfo>value=0x8008</xs:appinfo>
                </xs:annotation>
            </xs:enumeration>
        </xs:restriction>
    </xs:simpleType>
    <xs:simpleType name="gl_func_type">
        <xs:restriction base="xs:string">
            <xs:enumeration value="NEVER">
                <xs:annotation>
                    <xs:appinfo>value=0x0200</xs:appinfo>
                </xs:annotation>
            </xs:enumeration>
            <xs:enumeration value="LESS">
                <xs:annotation>
                    <xs:appinfo>value=0x0201</xs:appinfo>
                </xs:annotation>
            </xs:enumeration>
            <xs:enumeration value="LEQUAL">
                <xs:annotation>
                    <xs:appinfo>value=0x0203</xs:appinfo>
                </xs:annotation>
            </xs:enumeration>
            <xs:enumeration value="EQUAL">
                <xs:annotation>
                    <xs:appinfo>value=0x0202</xs:appinfo>
                </xs:annotation>
            </xs:enumeration>
            <xs:enumeration value="GREATER">
                <xs:annotation>
                    <xs:appinfo>value=0x0204</xs:appinfo>
                </xs:annotation>
            </xs:enumeration>
            <xs:enumeration value="NOTEQUAL">
                <xs:annotation>
                    <xs:appinfo>value=0x0205</xs:appinfo>
                </xs:annotation>
            </xs:enumeration>
            <xs:enumeration value="GEQUAL">
                <xs:annotation>
                    <xs:appinfo>value=0x0206</xs:appinfo>
                </xs:annotation>
            </xs:enumeration>
            <xs:enumeration value="ALWAYS">
                <xs:annotation>
                    <xs:appinfo>value=0x0207</xs:appinfo>
                </xs:annotation>
            </xs:enumeration>
        </xs:restriction>
    </xs:simpleType>
    <xs:simpleType name="gl_stencil_op_type">
        <xs:restriction base="xs:string">
            <xs:enumeration value="KEEP">
                <xs:annotation>
                    <xs:appinfo>value=0x1E00</xs:appinfo>
                </xs:annotation>
            </xs:enumeration>
            <xs:enumeration value="ZERO">
                <xs:annotation>
                    <xs:appinfo>value=0x0</xs:appinfo>
                </xs:annotation>
            </xs:enumeration>
            <xs:enumeration value="REPLACE">
                <xs:annotation>
                    <xs:appinfo>value=0x1E01</xs:appinfo>
                </xs:annotation>
            </xs:enumeration>
            <xs:enumeration value="INCR">
                <xs:annotation>
                    <xs:appinfo>value=0x1E02</xs:appinfo>
                </xs:annotation>
            </xs:enumeration>
            <xs:enumeration value="DECR">
                <xs:annotation>
                    <xs:appinfo>value=0x1E03</xs:appinfo>
                </xs:annotation>
            </xs:enumeration>
            <xs:enumeration value="INVERT">
                <xs:annotation>
                    <xs:appinfo>value=0x150A</xs:appinfo>
                </xs:annotation>
            </xs:enumeration>
            <xs:enumeration value="INCR_WRAP">
                <xs:annotation>
                    <xs:appinfo>value=0x8507</xs:appinfo>
                </xs:annotation>
            </xs:enumeration>
            <xs:enumeration value="DECR_WRAP">
                <xs:annotation>
                    <xs:appinfo>value=0x8508</xs:appinfo>
                </xs:annotation>
            </xs:enumeration>
        </xs:restriction>
    </xs:simpleType>
    <xs:simpleType name="gl_material_type">
        <xs:restriction base="xs:string">
            <xs:enumeration value="EMISSION">
                <xs:annotation>
                    <xs:appinfo>value=0x1600</xs:appinfo>
                </xs:annotation>
            </xs:enumeration>
            <xs:enumeration value="AMBIENT">
                <xs:annotation>
                    <xs:appinfo>value=0x1200</xs:appinfo>
                </xs:annotation>
            </xs:enumeration>
            <xs:enumeration value="DIFFUSE">
                <xs:annotation>
                    <xs:appinfo>value=0x1201</xs:appinfo>
                </xs:annotation>
            </xs:enumeration>
            <xs:enumeration value="SPECULAR">
                <xs:annotation>
                    <xs:appinfo>value=0x1202</xs:appinfo>
                </xs:annotation>
            </xs:enumeration>
            <xs:enumeration value="AMBIENT_AND_DIFFUSE">
                <xs:annotation>
                    <xs:appinfo>value=0x1602</xs:appinfo>
                </xs:annotation>
            </xs:enumeration>
        </xs:restriction>
    </xs:simpleType>
    <xs:simpleType name="gl_fog_type">
        <xs:restriction base="xs:string">
            <xs:enumeration value="LINEAR">
                <xs:annotation>
                    <xs:appinfo>value=0x2601</xs:appinfo>
                </xs:annotation>
            </xs:enumeration>
            <xs:enumeration value="EXP">
                <xs:annotation>
                    <xs:appinfo>value=0x0800</xs:appinfo>
                </xs:annotation>
            </xs:enumeration>
            <xs:enumeration value="EXP2">
                <xs:annotation>
                    <xs:appinfo>value=0x0801</xs:appinfo>
                </xs:annotation>
            </xs:enumeration>
        </xs:restriction>
    </xs:simpleType>
    <xs:simpleType name="gl_fog_coord_src_type">
        <xs:restriction base="xs:string">
            <xs:enumeration value="FOG_COORDINATE">
                <xs:annotation>
                    <xs:appinfo>value=0x8451</xs:appinfo>
                </xs:annotation>
            </xs:enumeration>
            <xs:enumeration value="FRAGMENT_DEPTH">
                <xs:annotation>
                    <xs:appinfo>value=0x8452</xs:appinfo>
                </xs:annotation>
            </xs:enumeration>
        </xs:restriction>
    </xs:simpleType>
    <xs:simpleType name="gl_front_face_type">
        <xs:restriction base="xs:string">
            <xs:enumeration value="CW">
                <xs:annotation>
                    <xs:appinfo>value=0x0900</xs:appinfo>
                </xs:annotation>
            </xs:enumeration>
            <xs:enumeration value="CCW">
                <xs:annotation>
                    <xs:appinfo>value=0x0901</xs:appinfo>
                </xs:annotation>
            </xs:enumeration>
        </xs:restriction>
    </xs:simpleType>
    <xs:simpleType name="gl_light_model_color_control_type">
        <xs:restriction base="xs:string">
            <xs:enumeration value="SINGLE_COLOR">
                <xs:annotation>
                    <xs:appinfo>value=0x81F9</xs:appinfo>
                </xs:annotation>
            </xs:enumeration>
            <xs:enumeration value="SEPARATE_SPECULAR_COLOR">
                <xs:annotation>
                    <xs:appinfo>value=0x81FA</xs:appinfo>
                </xs:annotation>
            </xs:enumeration>
        </xs:restriction>
    </xs:simpleType>
    <xs:simpleType name="gl_logic_op_type">
        <xs:restriction base="xs:string">
            <xs:enumeration value="CLEAR">
                <xs:annotation>
                    <xs:appinfo>value=0x1500</xs:appinfo>
                </xs:annotation>
            </xs:enumeration>
            <xs:enumeration value="AND">
                <xs:annotation>
                    <xs:appinfo>value=0x1501</xs:appinfo>
                </xs:annotation>
            </xs:enumeration>
            <xs:enumeration value="AND_REVERSE">
                <xs:annotation>
                    <xs:appinfo>value=0x1502</xs:appinfo>
                </xs:annotation>
            </xs:enumeration>
            <xs:enumeration value="COPY">
                <xs:annotation>
                    <xs:appinfo>value=0x1503</xs:appinfo>
                </xs:annotation>
            </xs:enumeration>
            <xs:enumeration value="AND_INVERTED">
                <xs:annotation>
                    <xs:appinfo>value=0x1504</xs:appinfo>
                </xs:annotation>
            </xs:enumeration>
            <xs:enumeration value="NOOP">
                <xs:annotation>
                    <xs:appinfo>value=0x1505</xs:appinfo>
                </xs:annotation>
            </xs:enumeration>
            <xs:enumeration value="XOR">
                <xs:annotation>
                    <xs:appinfo>value=0x1506</xs:appinfo>
                </xs:annotation>
            </xs:enumeration>
            <xs:enumeration value="OR">
                <xs:annotation>
                    <xs:appinfo>value=0x1507</xs:appinfo>
                </xs:annotation>
            </xs:enumeration>
            <xs:enumeration value="NOR">
                <xs:annotation>
                    <xs:appinfo>value=0x1508</xs:appinfo>
                </xs:annotation>
            </xs:enumeration>
            <xs:enumeration value="EQUIV">
                <xs:annotation>
                    <xs:appinfo>value=0x1509</xs:appinfo>
                </xs:annotation>
            </xs:enumeration>
            <xs:enumeration value="INVERT">
                <xs:annotation>
                    <xs:appinfo>value=0x150A</xs:appinfo>
                </xs:annotation>
            </xs:enumeration>
            <xs:enumeration value="OR_REVERSE">
                <xs:annotation>
                    <xs:appinfo>value=0x150B</xs:appinfo>
                </xs:annotation>
            </xs:enumeration>
            <xs:enumeration value="COPY_INVERTED">
                <xs:annotation>
                    <xs:appinfo>value=0x150C</xs:appinfo>
                </xs:annotation>
            </xs:enumeration>
            <xs:enumeration value="NAND">
                <xs:annotation>
                    <xs:appinfo>value=0x150E</xs:appinfo>
                </xs:annotation>
            </xs:enumeration>
            <xs:enumeration value="SET">
                <xs:annotation>
                    <xs:appinfo>value=0x150F</xs:appinfo>
                </xs:annotation>
            </xs:enumeration>
        </xs:restriction>
    </xs:simpleType>
    <xs:simpleType name="gl_polygon_mode_type">
        <xs:restriction base="xs:string">
            <xs:enumeration value="POINT">
                <xs:annotation>
                    <xs:appinfo>value=0x1B00</xs:appinfo>
                </xs:annotation>
            </xs:enumeration>
            <xs:enumeration value="LINE">
                <xs:annotation>
                    <xs:appinfo>value=0x1B01</xs:appinfo>
                </xs:annotation>
            </xs:enumeration>
            <xs:enumeration value="FILL">
                <xs:annotation>
                    <xs:appinfo>value=0x1B02</xs:appinfo>
                </xs:annotation>
            </xs:enumeration>
        </xs:restriction>
    </xs:simpleType>
    <xs:simpleType name="gl_shade_model_type">
        <xs:restriction base="xs:string">
            <xs:enumeration value="FLAT">
                <xs:annotation>
                    <xs:appinfo>value=0x1D00</xs:appinfo>
                </xs:annotation>
            </xs:enumeration>
            <xs:enumeration value="SMOOTH">
                <xs:annotation>
                    <xs:appinfo>value=0x1D01</xs:appinfo>
                </xs:annotation>
            </xs:enumeration>
        </xs:restriction>
    </xs:simpleType>
    <xs:simpleType name="gl_alpha_value_type">
        <xs:restriction base="xs:float">
            <xs:minInclusive value="0.0"/>
            <xs:maxInclusive value="1.0"/>
        </xs:restriction>
    </xs:simpleType>
    <xs:simpleType name="gl_enumeration">
        <xs:union memberTypes="gl_blend_type gl_face_type gl_blend_equation_type gl_func_type gl_stencil_op_type gl_material_type gl_fog_type gl_fog_coord_src_type gl_front_face_type gl_light_model_color_control_type gl_logic_op_type gl_polygon_mode_type gl_shade_model_type"/>
    </xs:simpleType>
    <xs:group name="gl_pipeline_settings">
        <xs:annotation>
            <xs:documentation>
            A group that defines all of the renderstates used for the CG and GLSL profiles.
            </xs:documentation>
        </xs:annotation>
        <xs:choice>
            <xs:element name="alpha_func">
                <xs:complexType>
                    <xs:sequence>
                        <xs:element name="func">
                            <xs:complexType>
                                <xs:attribute name="value" type="gl_func_type" use="optional" default="ALWAYS"/>
                                <xs:attribute name="param" type="xs:NCName" use="optional"/>
                            </xs:complexType>
                        </xs:element>
                        <xs:element name="value">
                            <xs:complexType>
                                <xs:attribute name="value" type="gl_alpha_value_type" use="optional" default="0.0"/>
                                <xs:attribute name="param" type="xs:NCName" use="optional"/>
                            </xs:complexType>
                        </xs:element>
                    </xs:sequence>
                </xs:complexType>
            </xs:element>
            <xs:element name="blend_func">
                <xs:complexType>
                    <xs:sequence>
                        <xs:element name="src">
                            <xs:complexType>
                                <xs:attribute name="value" type="gl_blend_type" use="optional" default="ONE"/>
                                <xs:attribute name="param" type="xs:NCName" use="optional"/>
                            </xs:complexType>
                        </xs:element>
                        <xs:element name="dest">
                            <xs:complexType>
                                <xs:attribute name="value" type="gl_blend_type" use="optional" default="ZERO"/>
                                <xs:attribute name="param" type="xs:NCName" use="optional"/>
                            </xs:complexType>
                        </xs:element>
                    </xs:sequence>
                </xs:complexType>
            </xs:element>
            <xs:element name="blend_func_separate">
                <xs:complexType>
                    <xs:sequence>
                        <xs:element name="src_rgb">
                            <xs:complexType>
                                <xs:attribute name="value" type="gl_blend_type" use="optional" default="ONE"/>
                                <xs:attribute name="param" type="xs:NCName" use="optional"/>
                            </xs:complexType>
                        </xs:element>
                        <xs:element name="dest_rgb">
                            <xs:complexType>
                                <xs:attribute name="value" type="gl_blend_type" use="optional" default="ZERO"/>
                                <xs:attribute name="param" type="xs:NCName" use="optional"/>
                            </xs:complexType>
                        </xs:element>
                        <xs:element name="src_alpha">
                            <xs:complexType>
                                <xs:attribute name="value" type="gl_blend_type" use="optional" default="ONE"/>
                                <xs:attribute name="param" type="xs:NCName" use="optional"/>
                            </xs:complexType>
                        </xs:element>
                        <xs:element name="dest_alpha">
                            <xs:complexType>
                                <xs:attribute name="value" type="gl_blend_type" use="optional" default="ZERO"/>
                                <xs:attribute name="param" type="xs:NCName" use="optional"/>
                            </xs:complexType>
                        </xs:element>
                    </xs:sequence>
                </xs:complexType>
            </xs:element>
            <xs:element name="blend_equation">
                <xs:complexType>
                    <xs:attribute name="value" type="gl_blend_equation_type" use="optional" default="FUNC_ADD"/>
                    <xs:attribute name="param" type="xs:NCName" use="optional"/>
                </xs:complexType>
            </xs:element>
            <xs:element name="blend_equation_separate">
                <xs:complexType>
                    <xs:sequence>
                        <xs:element name="rgb">
                            <xs:complexType>
                                <xs:attribute name="value" type="gl_blend_equation_type" use="optional" default="FUNC_ADD"/>
                                <xs:attribute name="param" type="xs:NCName" use="optional"/>
                            </xs:complexType>
                        </xs:element>
                        <xs:element name="alpha">
                            <xs:complexType>
                                <xs:attribute name="value" type="gl_blend_equation_type" use="optional" default="FUNC_ADD"/>
                                <xs:attribute name="param" type="xs:NCName" use="optional"/>
                            </xs:complexType>
                        </xs:element>
                    </xs:sequence>
                </xs:complexType>
            </xs:element>
            <xs:element name="color_material">
                <xs:complexType>
                    <xs:sequence>
                        <xs:element name="face">
                            <xs:complexType>
                                <xs:attribute name="value" type="gl_face_type" use="optional" default="FRONT_AND_BACK"/>
                                <xs:attribute name="param" type="xs:NCName" use="optional"/>
                            </xs:complexType>
                        </xs:element>
                        <xs:element name="mode">
                            <xs:complexType>
                                <xs:attribute name="value" type="gl_material_type" use="optional" default="AMBIENT_AND_DIFFUSE"/>
                                <xs:attribute name="param" type="xs:NCName" use="optional"/>
                            </xs:complexType>
                        </xs:element>
                    </xs:sequence>
                </xs:complexType>
            </xs:element>
            <xs:element name="cull_face">
                <xs:complexType>
                    <xs:attribute name="value" type="gl_face_type" use="optional" default="BACK"/>
                    <xs:attribute name="param" type="xs:NCName" use="optional"/>
                </xs:complexType>
            </xs:element>
            <xs:element name="depth_func">
                <xs:complexType>
                    <xs:attribute name="value" type="gl_func_type" use="optional" default="ALWAYS"/>
                    <xs:attribute name="param" type="xs:NCName" use="optional"/>
                </xs:complexType>
            </xs:element>
            <xs:element name="fog_mode">
                <xs:complexType>
                    <xs:attribute name="value" type="gl_fog_type" use="optional" default="EXP"/>
                    <xs:attribute name="param" type="xs:NCName" use="optional"/>
                </xs:complexType>
            </xs:element>
            <xs:element name="fog_coord_src">
                <xs:complexType>
                    <xs:attribute name="value" type="gl_fog_coord_src_type" use="optional" default="FOG_COORDINATE"/>
                    <xs:attribute name="param" type="xs:NCName" use="optional"/>
                </xs:complexType>
            </xs:element>
            <xs:element name="front_face">
                <xs:complexType>
                    <xs:attribute name="value" type="gl_front_face_type" use="optional" default="CCW"/>
                    <xs:attribute name="param" type="xs:NCName" use="optional"/>
                </xs:complexType>
            </xs:element>
            <xs:element name="light_model_color_control">
                <xs:complexType>
                    <xs:attribute name="value" type="gl_light_model_color_control_type" use="optional" default="SINGLE_COLOR"/>
                    <xs:attribute name="param" type="xs:NCName" use="optional"/>
                </xs:complexType>
            </xs:element>
            <xs:element name="logic_op">
                <xs:complexType>
                    <xs:attribute name="value" type="gl_logic_op_type" use="optional" default="COPY"/>
                    <xs:attribute name="param" type="xs:NCName" use="optional"/>
                </xs:complexType>
            </xs:element>
            <xs:element name="polygon_mode">
                <xs:complexType>
                    <xs:sequence>
                        <xs:element name="face">
                            <xs:complexType>
                                <xs:attribute name="value" type="gl_face_type" use="optional" default="FRONT_AND_BACK"/>
                                <xs:attribute name="param" type="xs:NCName" use="optional"/>
                            </xs:complexType>
                        </xs:element>
                        <xs:element name="mode">
                            <xs:complexType>
                                <xs:attribute name="value" type="gl_polygon_mode_type" use="optional" default="FILL"/>
                                <xs:attribute name="param" type="xs:NCName" use="optional"/>
                            </xs:complexType>
                        </xs:element>
                    </xs:sequence>
                </xs:complexType>
            </xs:element>
            <xs:element name="shade_model">
                <xs:complexType>
                    <xs:attribute name="value" type="gl_shade_model_type" use="optional" default="SMOOTH"/>
                    <xs:attribute name="param" type="xs:NCName" use="optional"/>
                </xs:complexType>
            </xs:element>
            <xs:element name="stencil_func">
                <xs:complexType>
                    <xs:sequence>
                        <xs:element name="func">
                            <xs:complexType>
                                <xs:attribute name="value" type="gl_func_type" use="optional" default="ALWAYS"/>
                                <xs:attribute name="param" type="xs:NCName" use="optional"/>
                            </xs:complexType>
                        </xs:element>
                        <xs:element name="ref">
                            <xs:complexType>
                                <xs:attribute name="value" type="xs:unsignedByte" use="optional" default="0"/>
                                <xs:attribute name="param" type="xs:NCName" use="optional"/>
                            </xs:complexType>
                        </xs:element>
                        <xs:element name="mask">
                            <xs:complexType>
                                <xs:attribute name="value" type="xs:unsignedByte" use="optional" default="255"/>
                                <xs:attribute name="param" type="xs:NCName" use="optional"/>
                            </xs:complexType>
                        </xs:element>
                    </xs:sequence>
                </xs:complexType>
            </xs:element>
            <xs:element name="stencil_op">
                <xs:complexType>
                    <xs:sequence>
                        <xs:element name="fail">
                            <xs:complexType>
                                <xs:attribute name="value" type="gl_stencil_op_type" use="optional" default="KEEP"/>
                                <xs:attribute name="param" type="xs:NCName" use="optional"/>
                            </xs:complexType>
                        </xs:element>
                        <xs:element name="zfail">
                            <xs:complexType>
                                <xs:attribute name="value" type="gl_stencil_op_type" use="optional" default="KEEP"/>
                                <xs:attribute name="param" type="xs:NCName" use="optional"/>
                            </xs:complexType>
                        </xs:element>
                        <xs:element name="zpass">
                            <xs:complexType>
                                <xs:attribute name="value" type="gl_stencil_op_type" use="optional" default="KEEP"/>
                                <xs:attribute name="param" type="xs:NCName" use="optional"/>
                            </xs:complexType>
                        </xs:element>
                    </xs:sequence>
                </xs:complexType>
            </xs:element>
            <xs:element name="stencil_func_separate">
                <xs:complexType>
                    <xs:sequence>
                        <xs:element name="front">
                            <xs:complexType>
                                <xs:attribute name="value" type="gl_func_type" use="optional" default="ALWAYS"/>
                                <xs:attribute name="param" type="xs:NCName" use="optional"/>
                            </xs:complexType>
                        </xs:element>
                        <xs:element name="back">
                            <xs:complexType>
                                <xs:attribute name="value" type="gl_func_type" use="optional" default="ALWAYS"/>
                                <xs:attribute name="param" type="xs:NCName" use="optional"/>
                            </xs:complexType>
                        </xs:element>
                        <xs:element name="ref">
                            <xs:complexType>
                                <xs:attribute name="value" type="xs:unsignedByte" use="optional" default="0"/>
                                <xs:attribute name="param" type="xs:NCName" use="optional"/>
                            </xs:complexType>
                        </xs:element>
                        <xs:element name="mask">
                            <xs:complexType>
                                <xs:attribute name="value" type="xs:unsignedByte" use="optional" default="255"/>
                                <xs:attribute name="param" type="xs:NCName" use="optional"/>
                            </xs:complexType>
                        </xs:element>
                    </xs:sequence>
                </xs:complexType>
            </xs:element>
            <xs:element name="stencil_op_separate">
                <xs:complexType>
                    <xs:sequence>
                        <xs:element name="face">
                            <xs:complexType>
                                <xs:attribute name="value" type="gl_face_type" use="optional" default="FRONT_AND_BACK"/>
                                <xs:attribute name="param" type="xs:NCName" use="optional"/>
                            </xs:complexType>
                        </xs:element>
                        <xs:element name="fail">
                            <xs:complexType>
                                <xs:attribute name="value" type="gl_stencil_op_type" use="optional" default="KEEP"/>
                                <xs:attribute name="param" type="xs:NCName" use="optional"/>
                            </xs:complexType>
                        </xs:element>
                        <xs:element name="zfail">
                            <xs:complexType>
                                <xs:attribute name="value" type="gl_stencil_op_type" use="optional" default="KEEP"/>
                                <xs:attribute name="param" type="xs:NCName" use="optional"/>
                            </xs:complexType>
                        </xs:element>
                        <xs:element name="zpass">
                            <xs:complexType>
                                <xs:attribute name="value" type="gl_stencil_op_type" use="optional" default="KEEP"/>
                                <xs:attribute name="param" type="xs:NCName" use="optional"/>
                            </xs:complexType>
                        </xs:element>
                    </xs:sequence>
                </xs:complexType>
            </xs:element>
            <xs:element name="stencil_mask_separate">
                <xs:complexType>
                    <xs:sequence>
                        <xs:element name="face">
                            <xs:complexType>
                                <xs:attribute name="value" type="gl_face_type" use="optional" default="FRONT_AND_BACK"/>
                                <xs:attribute name="param" type="xs:NCName" use="optional"/>
                            </xs:complexType>
                        </xs:element>
                        <xs:element name="mask">
                            <xs:complexType>
                                <xs:attribute name="value" type="xs:unsignedByte" use="optional" default="255"/>
                                <xs:attribute name="param" type="xs:NCName" use="optional"/>
                            </xs:complexType>
                        </xs:element>
                    </xs:sequence>
                </xs:complexType>
            </xs:element>
            <xs:element name="light_enable">
                <xs:complexType>
                    <xs:attribute name="value" type="bool" use="optional" default="false"/>
                    <xs:attribute name="param" type="xs:NCName" use="optional"/>
                    <xs:attribute name="index" type="GL_MAX_LIGHTS_index" use="required"/>
                </xs:complexType>
            </xs:element>
            <xs:element name="light_ambient">
                <xs:complexType>
                    <xs:attribute name="value" type="float4" use="optional" default="0 0 0 1"/>
                    <xs:attribute name="param" type="xs:NCName" use="optional"/>
                    <xs:attribute name="index" type="GL_MAX_LIGHTS_index" use="required"/>
                </xs:complexType>
            </xs:element>
            <xs:element name="light_diffuse">
                <xs:complexType>
                    <xs:attribute name="value" type="float4" use="optional" default="0 0 0 0"/>
                    <xs:attribute name="param" type="xs:NCName" use="optional"/>
                    <xs:attribute name="index" type="GL_MAX_LIGHTS_index" use="required"/>
                </xs:complexType>
            </xs:element>
            <xs:element name="light_specular">
                <xs:complexType>
                    <xs:attribute name="value" type="float4" use="optional" default="0 0 0 0"/>
                    <xs:attribute name="param" type="xs:NCName" use="optional"/>
                    <xs:attribute name="index" type="GL_MAX_LIGHTS_index" use="required"/>
                </xs:complexType>
            </xs:element>
            <xs:element name="light_position">
                <xs:complexType>
                    <xs:attribute name="value" type="float4" use="optional" default="0 0 1 0"/>
                    <xs:attribute name="param" type="xs:NCName" use="optional"/>
                    <xs:attribute name="index" type="GL_MAX_LIGHTS_index" use="required"/>
                </xs:complexType>
            </xs:element>
            <xs:element name="light_constant_attenuation">
                <xs:complexType>
                    <xs:attribute name="value" type="float" use="optional" default="1"/>
                    <xs:attribute name="param" type="xs:NCName" use="optional"/>
                    <xs:attribute name="index" type="GL_MAX_LIGHTS_index" use="required"/>
                </xs:complexType>
            </xs:element>
            <xs:element name="light_linear_attenuation">
                <xs:complexType>
                    <xs:attribute name="value" type="float" use="optional" default="0"/>
                    <xs:attribute name="param" type="xs:NCName" use="optional"/>
                    <xs:attribute name="index" type="GL_MAX_LIGHTS_index" use="required"/>
                </xs:complexType>
            </xs:element>
            <xs:element name="light_quadratic_attenuation">
                <xs:complexType>
                    <xs:attribute name="value" type="float" use="optional" default="0"/>
                    <xs:attribute name="param" type="xs:NCName" use="optional"/>
                    <xs:attribute name="index" type="GL_MAX_LIGHTS_index" use="required"/>
                </xs:complexType>
            </xs:element>
            <xs:element name="light_spot_cutoff">
                <xs:complexType>
                    <xs:attribute name="value" type="float" use="optional" default="180"/>
                    <xs:attribute name="param" type="xs:NCName" use="optional"/>
                    <xs:attribute name="index" type="GL_MAX_LIGHTS_index" use="required"/>
                </xs:complexType>
            </xs:element>
            <xs:element name="light_spot_direction">
                <xs:complexType>
                    <xs:attribute name="value" type="float3" use="optional" default="0 0 -1"/>
                    <xs:attribute name="param" type="xs:NCName" use="optional"/>
                    <xs:attribute name="index" type="GL_MAX_LIGHTS_index" use="required"/>
                </xs:complexType>
            </xs:element>
            <xs:element name="light_spot_exponent">
                <xs:complexType>
                    <xs:attribute name="value" type="float" use="optional" default="0"/>
                    <xs:attribute name="param" type="xs:NCName" use="optional"/>
                    <xs:attribute name="index" type="GL_MAX_LIGHTS_index" use="required"/>
                </xs:complexType>
            </xs:element>
            <xs:element name="texture1D">
                <xs:complexType>
                    <xs:choice>
                        <xs:element name="value" type="gl_sampler1D"/>
                        <xs:element name="param" type="xs:NCName"/>
                    </xs:choice>
                    <xs:attribute name="index" type="GL_MAX_TEXTURE_IMAGE_UNITS_index" use="required"/>
                </xs:complexType>
            </xs:element>
            <xs:element name="texture2D">
                <xs:complexType>
                    <xs:choice>
                        <xs:element name="value" type="gl_sampler2D"/>
                        <xs:element name="param" type="xs:NCName"/>
                    </xs:choice>
                    <xs:attribute name="index" type="GL_MAX_TEXTURE_IMAGE_UNITS_index" use="required"/>
                </xs:complexType>
            </xs:element>
            <xs:element name="texture3D">
                <xs:complexType>
                    <xs:choice>
                        <xs:element name="value" type="gl_sampler3D"/>
                        <xs:element name="param" type="xs:NCName"/>
                    </xs:choice>
                    <xs:attribute name="index" type="GL_MAX_TEXTURE_IMAGE_UNITS_index" use="required"/>
                </xs:complexType>
            </xs:element>
            <xs:element name="textureCUBE">
                <xs:complexType>
                    <xs:choice>
                        <xs:element name="value" type="gl_samplerCUBE"/>
                        <xs:element name="param" type="xs:NCName"/>
                    </xs:choice>
                    <xs:attribute name="index" type="GL_MAX_TEXTURE_IMAGE_UNITS_index" use="required"/>
                </xs:complexType>
            </xs:element>
            <xs:element name="textureRECT">
                <xs:complexType>
                    <xs:choice>
                        <xs:element name="value" type="gl_samplerRECT"/>
                        <xs:element name="param" type="xs:NCName"/>
                    </xs:choice>
                    <xs:attribute name="index" type="GL_MAX_TEXTURE_IMAGE_UNITS_index" use="required"/>
                </xs:complexType>
            </xs:element>
            <xs:element name="textureDEPTH">
                <xs:complexType>
                    <xs:choice>
                        <xs:element name="value" type="gl_samplerDEPTH"/>
                        <xs:element name="param" type="xs:NCName"/>
                    </xs:choice>
                    <xs:attribute name="index" type="GL_MAX_TEXTURE_IMAGE_UNITS_index" use="required"/>
                </xs:complexType>
            </xs:element>
            <xs:element name="texture1D_enable">
                <xs:complexType>
                    <xs:attribute name="value" type="bool" use="optional" default="false"/>
                    <xs:attribute name="param" type="xs:NCName" use="optional"/>
                    <xs:attribute name="index" type="GL_MAX_TEXTURE_IMAGE_UNITS_index"/>
                </xs:complexType>
            </xs:element>
            <xs:element name="texture2D_enable">
                <xs:complexType>
                    <xs:attribute name="value" type="bool" use="optional" default="false"/>
                    <xs:attribute name="param" type="xs:NCName" use="optional"/>
                    <xs:attribute name="index" type="GL_MAX_TEXTURE_IMAGE_UNITS_index"/>
                </xs:complexType>
            </xs:element>
            <xs:element name="texture3D_enable">
                <xs:complexType>
                    <xs:attribute name="value" type="bool" use="optional" default="false"/>
                    <xs:attribute name="param" type="xs:NCName" use="optional"/>
                    <xs:attribute name="index" type="GL_MAX_TEXTURE_IMAGE_UNITS_index"/>
                </xs:complexType>
            </xs:element>
            <xs:element name="textureCUBE_enable">
                <xs:complexType>
                    <xs:attribute name="value" type="bool" use="optional" default="false"/>
                    <xs:attribute name="param" type="xs:NCName" use="optional"/>
                    <xs:attribute name="index" type="GL_MAX_TEXTURE_IMAGE_UNITS_index"/>
                </xs:complexType>
            </xs:element>
            <xs:element name="textureRECT_enable">
                <xs:complexType>
                    <xs:attribute name="value" type="bool" use="optional" default="false"/>
                    <xs:attribute name="param" type="xs:NCName" use="optional"/>
                    <xs:attribute name="index" type="GL_MAX_TEXTURE_IMAGE_UNITS_index"/>
                </xs:complexType>
            </xs:element>
            <xs:element name="textureDEPTH_enable">
                <xs:complexType>
                    <xs:attribute name="value" type="bool" use="optional" default="false"/>
                    <xs:attribute name="param" type="xs:NCName" use="optional"/>
                    <xs:attribute name="index" type="GL_MAX_TEXTURE_IMAGE_UNITS_index"/>
                </xs:complexType>
            </xs:element>
            <xs:element name="texture_env_color">
                <xs:complexType>
                    <xs:attribute name="value" type="float4" use="optional"/>
                    <xs:attribute name="param" type="xs:NCName" use="optional"/>
                    <xs:attribute name="index" type="GL_MAX_TEXTURE_IMAGE_UNITS_index"/>
                </xs:complexType>
            </xs:element>
            <xs:element name="texture_env_mode">
                <xs:complexType>
                    <xs:attribute name="value" type="string" use="optional"/>
                    <xs:attribute name="param" type="xs:NCName" use="optional"/>
                    <xs:attribute name="index" type="GL_MAX_TEXTURE_IMAGE_UNITS_index"/>
                </xs:complexType>
            </xs:element>
            <xs:element name="clip_plane">
                <xs:complexType>
                    <xs:attribute name="value" type="float4" use="optional" default="0 0 0 0"/>
                    <xs:attribute name="param" type="xs:NCName" use="optional"/>
                    <xs:attribute name="index" type="GL_MAX_CLIP_PLANES_index"/>
                </xs:complexType>
            </xs:element>
            <xs:element name="clip_plane_enable">
                <xs:complexType>
                    <xs:attribute name="value" type="bool" use="optional" default="false"/>
                    <xs:attribute name="param" type="xs:NCName" use="optional"/>
                    <xs:attribute name="index" type="GL_MAX_CLIP_PLANES_index"/>
                </xs:complexType>
            </xs:element>
            <xs:element name="blend_color">
                <xs:complexType>
                    <xs:attribute name="value" type="float4" use="optional" default="0 0 0 0"/>
                    <xs:attribute name="param" type="xs:NCName" use="optional"/>
                </xs:complexType>
            </xs:element>
            <xs:element name="clear_color">
                <xs:complexType>
                    <xs:attribute name="value" type="float4" use="optional" default="0 0 0 0"/>
                    <xs:attribute name="param" type="xs:NCName" use="optional"/>
                </xs:complexType>
            </xs:element>
            <xs:element name="clear_stencil">
                <xs:complexType>
                    <xs:attribute name="value" type="int" use="optional" default="0"/>
                    <xs:attribute name="param" type="xs:NCName" use="optional"/>
                </xs:complexType>
            </xs:element>
            <xs:element name="clear_depth">
                <xs:complexType>
                    <xs:attribute name="value" type="float" use="optional" default="1"/>
                    <xs:attribute name="param" type="xs:NCName" use="optional"/>
                </xs:complexType>
            </xs:element>
            <xs:element name="color_mask">
                <xs:complexType>
                    <xs:attribute name="value" type="bool4" use="optional" default="true true true true"/>
                    <xs:attribute name="param" type="xs:NCName" use="optional"/>
                </xs:complexType>
            </xs:element>
            <xs:element name="depth_bounds">
                <xs:complexType>
                    <xs:attribute name="value" type="float2" use="optional"/>
                    <xs:attribute name="param" type="xs:NCName" use="optional"/>
                </xs:complexType>
            </xs:element>
            <xs:element name="depth_mask">
                <xs:complexType>
                    <xs:attribute name="value" type="bool" use="optional" default="true"/>
                    <xs:attribute name="param" type="xs:NCName" use="optional"/>
                </xs:complexType>
            </xs:element>
            <xs:element name="depth_range">
                <xs:complexType>
                    <xs:attribute name="value" type="float2" use="optional" default="0 1"/>
                    <xs:attribute name="param" type="xs:NCName" use="optional"/>
                </xs:complexType>
            </xs:element>
            <xs:element name="fog_density">
                <xs:complexType>
                    <xs:attribute name="value" type="float" use="optional" default="1"/>
                    <xs:attribute name="param" type="xs:NCName" use="optional"/>
                </xs:complexType>
            </xs:element>
            <xs:element name="fog_start">
                <xs:complexType>
                    <xs:attribute name="value" type="float" use="optional" default="0"/>
                    <xs:attribute name="param" type="xs:NCName" use="optional"/>
                </xs:complexType>
            </xs:element>
            <xs:element name="fog_end">
                <xs:complexType>
                    <xs:attribute name="value" type="float" use="optional" default="1"/>
                    <xs:attribute name="param" type="xs:NCName" use="optional"/>
                </xs:complexType>
            </xs:element>
            <xs:element name="fog_color">
                <xs:complexType>
                    <xs:attribute name="value" type="float4" use="optional" default="0 0 0 0"/>
                    <xs:attribute name="param" type="xs:NCName" use="optional"/>
                </xs:complexType>
            </xs:element>
            <xs:element name="light_model_ambient">
                <xs:complexType>
                    <xs:attribute name="value" type="float4" use="optional" default="0.2 0.2 0.2 1.0"/>
                    <xs:attribute name="param" type="xs:NCName" use="optional"/>
                </xs:complexType>
            </xs:element>
            <xs:element name="lighting_enable">
                <xs:complexType>
                    <xs:attribute name="value" type="bool" use="optional" default="false"/>
                    <xs:attribute name="param" type="xs:NCName" use="optional"/>
                </xs:complexType>
            </xs:element>
            <xs:element name="line_stipple">
                <xs:complexType>
                    <xs:attribute name="value" type="int2" use="optional" default="1 65536"/>
                    <xs:attribute name="param" type="xs:NCName" use="optional"/>
                </xs:complexType>
            </xs:element>
            <xs:element name="line_width">
                <xs:complexType>
                    <xs:attribute name="value" type="float" use="optional" default="1"/>
                    <xs:attribute name="param" type="xs:NCName" use="optional"/>
                </xs:complexType>
            </xs:element>
            <xs:element name="material_ambient">
                <xs:complexType>
                    <xs:attribute name="value" type="float4" use="optional" default="0.2 0.2 0.2 1.0"/>
                    <xs:attribute name="param" type="xs:NCName" use="optional"/>
                </xs:complexType>
            </xs:element>
            <xs:element name="material_diffuse">
                <xs:complexType>
                    <xs:attribute name="value" type="float4" use="optional" default="0.8 0.8 0.8 1.0"/>
                    <xs:attribute name="param" type="xs:NCName" use="optional"/>
                </xs:complexType>
            </xs:element>
            <xs:element name="material_emission">
                <xs:complexType>
                    <xs:attribute name="value" type="float4" use="optional" default="0 0 0 1"/>
                    <xs:attribute name="param" type="xs:NCName" use="optional"/>
                </xs:complexType>
            </xs:element>
            <xs:element name="material_shininess">
                <xs:complexType>
                    <xs:attribute name="value" type="float" use="optional" default="0"/>
                    <xs:attribute name="param" type="xs:NCName" use="optional"/>
                </xs:complexType>
            </xs:element>
            <xs:element name="material_specular">
                <xs:complexType>
                    <xs:attribute name="value" type="float4" use="optional" default="0 0 0 1"/>
                    <xs:attribute name="param" type="xs:NCName" use="optional"/>
                </xs:complexType>
            </xs:element>
            <xs:element name="model_view_matrix">
                <xs:complexType>
                    <xs:attribute name="value" type="float4x4" use="optional" default="1 0 0 0 0 1 0 0 0 0 1 0 0 0 0 1"/>
                    <xs:attribute name="param" type="xs:NCName" use="optional"/>
                </xs:complexType>
            </xs:element>
            <xs:element name="point_distance_attenuation">
                <xs:complexType>
                    <xs:attribute name="value" type="float3" use="optional" default="1 0 0"/>
                    <xs:attribute name="param" type="xs:NCName" use="optional"/>
                </xs:complexType>
            </xs:element>
            <xs:element name="point_fade_threshold_size">
                <xs:complexType>
                    <xs:attribute name="value" type="float" use="optional" default="1"/>
                    <xs:attribute name="param" type="xs:NCName" use="optional"/>
                </xs:complexType>
            </xs:element>
            <xs:element name="point_size">
                <xs:complexType>
                    <xs:attribute name="value" type="float" use="optional" default="1"/>
                    <xs:attribute name="param" type="xs:NCName" use="optional"/>
                </xs:complexType>
            </xs:element>
            <xs:element name="point_size_min">
                <xs:complexType>
                    <xs:attribute name="value" type="float" use="optional" default="0"/>
                    <xs:attribute name="param" type="xs:NCName" use="optional"/>
                </xs:complexType>
            </xs:element>
            <xs:element name="point_size_max">
                <xs:complexType>
                    <xs:attribute name="value" type="float" use="optional" default="1"/>
                    <xs:attribute name="param" type="xs:NCName" use="optional"/>
                </xs:complexType>
            </xs:element>
            <xs:element name="polygon_offset">
                <xs:complexType>
                    <xs:attribute name="value" type="float2" use="optional" default="0 0"/>
                    <xs:attribute name="param" type="xs:NCName" use="optional"/>
                </xs:complexType>
            </xs:element>
            <xs:element name="projection_matrix">
                <xs:complexType>
                    <xs:attribute name="value" type="float4x4" use="optional" default="1 0 0 0 0 1 0 0 0 0 1 0 0 0 0 1"/>
                    <xs:attribute name="param" type="xs:NCName" use="optional"/>
                </xs:complexType>
            </xs:element>
            <xs:element name="scissor">
                <xs:complexType>
                    <xs:attribute name="value" type="int4" use="optional"/>
                    <xs:attribute name="param" type="xs:NCName" use="optional"/>
                </xs:complexType>
            </xs:element>
            <xs:element name="stencil_mask">
                <xs:complexType>
                    <xs:attribute name="value" type="int" use="optional" default="4294967295"/>
                    <xs:attribute name="param" type="xs:NCName" use="optional"/>
                </xs:complexType>
            </xs:element>
            <xs:element name="alpha_test_enable">
                <xs:complexType>
                    <xs:attribute name="value" type="bool" use="optional" default="false"/>
                    <xs:attribute name="param" type="xs:NCName" use="optional"/>
                </xs:complexType>
            </xs:element>
            <xs:element name="auto_normal_enable">
                <xs:complexType>
                    <xs:attribute name="value" type="bool" use="optional" default="false"/>
                    <xs:attribute name="param" type="xs:NCName" use="optional"/>
                </xs:complexType>
            </xs:element>
            <xs:element name="blend_enable">
                <xs:complexType>
                    <xs:attribute name="value" type="bool" use="optional" default="false"/>
                    <xs:attribute name="param" type="xs:NCName" use="optional"/>
                </xs:complexType>
            </xs:element>
            <xs:element name="color_logic_op_enable">
                <xs:complexType>
                    <xs:attribute name="value" type="bool" use="optional" default="false"/>
                    <xs:attribute name="param" type="xs:NCName" use="optional"/>
                </xs:complexType>
            </xs:element>
            <xs:element name="color_material_enable">
                <xs:complexType>
                    <xs:attribute name="value" type="bool" use="optional" default="true"/>
                    <xs:attribute name="param" type="xs:NCName" use="optional"/>
                </xs:complexType>
            </xs:element>
            <xs:element name="cull_face_enable">
                <xs:complexType>
                    <xs:attribute name="value" type="bool" use="optional" default="false"/>
                    <xs:attribute name="param" type="xs:NCName" use="optional"/>
                </xs:complexType>
            </xs:element>
            <xs:element name="depth_bounds_enable">
                <xs:complexType>
                    <xs:attribute name="value" type="bool" use="optional" default="false"/>
                    <xs:attribute name="param" type="xs:NCName" use="optional"/>
                </xs:complexType>
            </xs:element>
            <xs:element name="depth_clamp_enable">
                <xs:complexType>
                    <xs:attribute name="value" type="bool" use="optional" default="false"/>
                    <xs:attribute name="param" type="xs:NCName" use="optional"/>
                </xs:complexType>
            </xs:element>
            <xs:element name="depth_test_enable">
                <xs:complexType>
                    <xs:attribute name="value" type="bool" use="optional" default="false"/>
                    <xs:attribute name="param" type="xs:NCName" use="optional"/>
                </xs:complexType>
            </xs:element>
            <xs:element name="dither_enable">
                <xs:complexType>
                    <xs:attribute name="value" type="bool" use="optional" default="true"/>
                    <xs:attribute name="param" type="xs:NCName" use="optional"/>
                </xs:complexType>
            </xs:element>
            <xs:element name="fog_enable">
                <xs:complexType>
                    <xs:attribute name="value" type="bool" use="optional" default="false"/>
                    <xs:attribute name="param" type="xs:NCName" use="optional"/>
                </xs:complexType>
            </xs:element>
            <xs:element name="light_model_local_viewer_enable">
                <xs:complexType>
                    <xs:attribute name="value" type="bool" use="optional" default="false"/>
                    <xs:attribute name="param" type="xs:NCName" use="optional"/>
                </xs:complexType>
            </xs:element>
            <xs:element name="light_model_two_side_enable">
                <xs:complexType>
                    <xs:attribute name="value" type="bool" use="optional" default="false"/>
                    <xs:attribute name="param" type="xs:NCName" use="optional"/>
                </xs:complexType>
            </xs:element>
            <xs:element name="line_smooth_enable">
                <xs:complexType>
                    <xs:attribute name="value" type="bool" use="optional" default="false"/>
                    <xs:attribute name="param" type="xs:NCName" use="optional"/>
                </xs:complexType>
            </xs:element>
            <xs:element name="line_stipple_enable">
                <xs:complexType>
                    <xs:attribute name="value" type="bool" use="optional" default="false"/>
                    <xs:attribute name="param" type="xs:NCName" use="optional"/>
                </xs:complexType>
            </xs:element>
            <xs:element name="logic_op_enable">
                <xs:complexType>
                    <xs:attribute name="value" type="bool" use="optional" default="false"/>
                    <xs:attribute name="param" type="xs:NCName" use="optional"/>
                </xs:complexType>
            </xs:element>
            <xs:element name="multisample_enable">
                <xs:complexType>
                    <xs:attribute name="value" type="bool" use="optional" default="false"/>
                    <xs:attribute name="param" type="xs:NCName" use="optional"/>
                </xs:complexType>
            </xs:element>
            <xs:element name="normalize_enable">
                <xs:complexType>
                    <xs:attribute name="value" type="bool" use="optional" default="false"/>
                    <xs:attribute name="param" type="xs:NCName" use="optional"/>
                </xs:complexType>
            </xs:element>
            <xs:element name="point_smooth_enable">
                <xs:complexType>
                    <xs:attribute name="value" type="bool" use="optional" default="false"/>
                    <xs:attribute name="param" type="xs:NCName" use="optional"/>
                </xs:complexType>
            </xs:element>
            <xs:element name="polygon_offset_fill_enable">
                <xs:complexType>
                    <xs:attribute name="value" type="bool" use="optional" default="false"/>
                    <xs:attribute name="param" type="xs:NCName" use="optional"/>
                </xs:complexType>
            </xs:element>
            <xs:element name="polygon_offset_line_enable">
                <xs:complexType>
                    <xs:attribute name="value" type="bool" use="optional" default="false"/>
                    <xs:attribute name="param" type="xs:NCName" use="optional"/>
                </xs:complexType>
            </xs:element>
            <xs:element name="polygon_offset_point_enable">
                <xs:complexType>
                    <xs:attribute name="value" type="bool" use="optional" default="false"/>
                    <xs:attribute name="param" type="xs:NCName" use="optional"/>
                </xs:complexType>
            </xs:element>
            <xs:element name="polygon_smooth_enable">
                <xs:complexType>
                    <xs:attribute name="value" type="bool" use="optional" default="false"/>
                    <xs:attribute name="param" type="xs:NCName" use="optional"/>
                </xs:complexType>
            </xs:element>
            <xs:element name="polygon_stipple_enable">
                <xs:complexType>
                    <xs:attribute name="value" type="bool" use="optional" default="false"/>
                    <xs:attribute name="param" type="xs:NCName" use="optional"/>
                </xs:complexType>
            </xs:element>
            <xs:element name="rescale_normal_enable">
                <xs:complexType>
                    <xs:attribute name="value" type="bool" use="optional" default="false"/>
                    <xs:attribute name="param" type="xs:NCName" use="optional"/>
                </xs:complexType>
            </xs:element>
            <xs:element name="sample_alpha_to_coverage_enable">
                <xs:complexType>
                    <xs:attribute name="value" type="bool" use="optional" default="false"/>
                    <xs:attribute name="param" type="xs:NCName" use="optional"/>
                </xs:complexType>
            </xs:element>
            <xs:element name="sample_alpha_to_one_enable">
                <xs:complexType>
                    <xs:attribute name="value" type="bool" use="optional" default="false"/>
                    <xs:attribute name="param" type="xs:NCName" use="optional"/>
                </xs:complexType>
            </xs:element>
            <xs:element name="sample_coverage_enable">
                <xs:complexType>
                    <xs:attribute name="value" type="bool" use="optional" default="false"/>
                    <xs:attribute name="param" type="xs:NCName" use="optional"/>
                </xs:complexType>
            </xs:element>
            <xs:element name="scissor_test_enable">
                <xs:complexType>
                    <xs:attribute name="value" type="bool" use="optional" default="false"/>
                    <xs:attribute name="param" type="xs:NCName" use="optional"/>
                </xs:complexType>
            </xs:element>
            <xs:element name="stencil_test_enable">
                <xs:complexType>
                    <xs:attribute name="value" type="bool" use="optional" default="false"/>
                    <xs:attribute name="param" type="xs:NCName" use="optional"/>
                </xs:complexType>
            </xs:element>
            <xs:element ref="gl_hook_abstract"/>
        </xs:choice>
    </xs:group>
    <xs:element name="gl_hook_abstract" abstract="true"/>
    <xs:simpleType name="glsl_float">
        <xs:restriction base="xs:float"/>
    </xs:simpleType>
    <xs:simpleType name="glsl_int">
        <xs:restriction base="xs:int"/>
    </xs:simpleType>
    <xs:simpleType name="glsl_bool">
        <xs:restriction base="xs:boolean"/>
    </xs:simpleType>
    <xs:simpleType name="glsl_ListOfBool">
        <xs:list itemType="glsl_bool"/>
    </xs:simpleType>
    <xs:simpleType name="glsl_ListOfFloat">
        <xs:list itemType="glsl_float"/>
    </xs:simpleType>
    <xs:simpleType name="glsl_ListOfInt">
        <xs:list itemType="glsl_int"/>
    </xs:simpleType>
    <xs:simpleType name="glsl_bool2">
        <xs:restriction base="glsl_ListOfBool">
            <xs:minLength value="2"/>
            <xs:maxLength value="2"/>
        </xs:restriction>
    </xs:simpleType>
    <xs:simpleType name="glsl_bool3">
        <xs:restriction base="glsl_ListOfBool">
            <xs:minLength value="3"/>
            <xs:maxLength value="3"/>
        </xs:restriction>
    </xs:simpleType>
    <xs:simpleType name="glsl_bool4">
        <xs:restriction base="glsl_ListOfBool">
            <xs:minLength value="4"/>
            <xs:maxLength value="4"/>
        </xs:restriction>
    </xs:simpleType>
    <xs:simpleType name="glsl_float2">
        <xs:restriction base="glsl_ListOfFloat">
            <xs:minLength value="2"/>
            <xs:maxLength value="2"/>
        </xs:restriction>
    </xs:simpleType>
    <xs:simpleType name="glsl_float3">
        <xs:restriction base="glsl_ListOfFloat">
            <xs:minLength value="3"/>
            <xs:maxLength value="3"/>
        </xs:restriction>
    </xs:simpleType>
    <xs:simpleType name="glsl_float4">
        <xs:restriction base="glsl_ListOfFloat">
            <xs:minLength value="4"/>
            <xs:maxLength value="4"/>
        </xs:restriction>
    </xs:simpleType>
    <xs:simpleType name="glsl_float2x2">
        <xs:restriction base="glsl_ListOfFloat">
            <xs:minLength value="4"/>
            <xs:maxLength value="4"/>
        </xs:restriction>
    </xs:simpleType>
    <xs:simpleType name="glsl_float3x3">
        <xs:restriction base="glsl_ListOfFloat">
            <xs:minLength value="9"/>
            <xs:maxLength value="9"/>
        </xs:restriction>
    </xs:simpleType>
    <xs:simpleType name="glsl_float4x4">
        <xs:restriction base="glsl_ListOfFloat">
            <xs:minLength value="16"/>
            <xs:maxLength value="16"/>
        </xs:restriction>
    </xs:simpleType>
    <xs:simpleType name="glsl_int2">
        <xs:restriction base="glsl_ListOfInt">
            <xs:minLength value="2"/>
            <xs:maxLength value="2"/>
        </xs:restriction>
    </xs:simpleType>
    <xs:simpleType name="glsl_int3">
        <xs:restriction base="glsl_ListOfInt">
            <xs:minLength value="3"/>
            <xs:maxLength value="3"/>
        </xs:restriction>
    </xs:simpleType>
    <xs:simpleType name="glsl_int4">
        <xs:restriction base="glsl_ListOfInt">
            <xs:minLength value="4"/>
            <xs:maxLength value="4"/>
        </xs:restriction>
    </xs:simpleType>
    <xs:simpleType name="glsl_pipeline_stage">
        <xs:restriction base="xs:string">
            <xs:enumeration value="VERTEXPROGRAM"/>
            <xs:enumeration value="FRAGMENTPROGRAM"/>
        </xs:restriction>
    </xs:simpleType>
    <xs:simpleType name="glsl_identifier">
        <xs:restriction base="xs:token"/>
    </xs:simpleType>
    <xs:complexType name="glsl_newarray_type">
        <xs:annotation>
            <xs:documentation>
            The glsl_newarray_type is used to creates a parameter of a one-dimensional array type.
            </xs:documentation>
        </xs:annotation>
        <xs:choice minOccurs="0" maxOccurs="unbounded">
            <xs:group ref="glsl_param_type"/>
            <xs:element name="array" type="glsl_newarray_type">
                <xs:annotation>
                    <xs:documentation>
                    You may recursively nest glsl_newarray elements to create multidimensional arrays.
                    </xs:documentation>
                </xs:annotation>
            </xs:element>
        </xs:choice>
        <xs:attribute name="length" type="xs:positiveInteger" use="required">
            <xs:annotation>
                <xs:documentation>
                The length attribute specifies the length of the array.
                </xs:documentation>
            </xs:annotation>
        </xs:attribute>
    </xs:complexType>
    <xs:complexType name="glsl_setarray_type">
        <xs:annotation>
            <xs:documentation>
            The glsl_newarray_type is used to creates a parameter of a one-dimensional array type.
            </xs:documentation>
        </xs:annotation>
        <xs:choice minOccurs="0" maxOccurs="unbounded">
            <xs:group ref="glsl_param_type"/>
            <xs:element name="array" type="glsl_setarray_type">
                <xs:annotation>
                    <xs:documentation>
                    You may recursively nest glsl_newarray elements to create multidimensional arrays.
                    </xs:documentation>
                </xs:annotation>
            </xs:element>
        </xs:choice>
        <xs:attribute name="length" type="xs:positiveInteger" use="optional">
            <xs:annotation>
                <xs:documentation>
                The length attribute specifies the length of the array.
                </xs:documentation>
            </xs:annotation>
        </xs:attribute>
    </xs:complexType>
    <xs:complexType name="glsl_surface_type">
        <xs:annotation>
            <xs:documentation>
            A surface type for the GLSL profile. This surface inherits from the fx_surface_common type and adds the
            ability to programmatically generate textures.
            </xs:documentation>
        </xs:annotation>
        <xs:complexContent>
            <xs:extension base="fx_surface_common">
                <xs:sequence>
                    <xs:element name="generator" minOccurs="0">
                        <xs:annotation>
                            <xs:documentation>
                            A procedural surface generator.
                            </xs:documentation>
                        </xs:annotation>
                        <xs:complexType>
                            <xs:sequence>
                                <xs:element name="annotate" type="fx_annotate_common" minOccurs="0" maxOccurs="unbounded">
                                    <xs:annotation>
                                        <xs:documentation>
                                        The annotate element allows you to specify an annotation for this surface generator.
                                        </xs:documentation>
                                    </xs:annotation>
                                </xs:element>
                                <xs:choice maxOccurs="unbounded">
                                    <xs:element name="code" type="fx_code_profile">
                                        <xs:annotation>
                                            <xs:documentation>
                                            The code element allows you to embed GLSL code to use for this surface generator.
                                            </xs:documentation>
                                        </xs:annotation>
                                    </xs:element>
                                    <xs:element name="include" type="fx_include_common">
                                        <xs:annotation>
                                            <xs:documentation>
                                            The include element allows you to import GLSL code to use for this surface generator.
                                            </xs:documentation>
                                        </xs:annotation>
                                    </xs:element>
                                </xs:choice>
                                <xs:element name="name">
                                    <xs:annotation>
                                        <xs:documentation>
                                        The entry symbol for the shader function.
                                        </xs:documentation>
                                    </xs:annotation>
                                    <xs:complexType>
                                        <xs:simpleContent>
                                            <xs:extension base="xs:NCName">
                                                <xs:attribute name="source" type="xs:NCName" use="optional"/>
                                            </xs:extension>
                                        </xs:simpleContent>
                                    </xs:complexType>
                                </xs:element>
                                <xs:element name="setparam" type="glsl_setparam_simple" minOccurs="0" maxOccurs="unbounded">
                                    <xs:annotation>
                                        <xs:documentation>
                                        The setparam element allows you to assign a new value to a previously defined parameter.
                                        </xs:documentation>
                                    </xs:annotation>
                                </xs:element>
                            </xs:sequence>
                        </xs:complexType>
                    </xs:element>
                </xs:sequence>
            </xs:extension>
        </xs:complexContent>
    </xs:complexType>
    <xs:group name="glsl_param_type">
        <xs:annotation>
            <xs:documentation>
            A group that specifies the allowable types for GLSL profile parameters.
            </xs:documentation>
        </xs:annotation>
        <xs:choice>
            <xs:element name="bool" type="glsl_bool"/>
            <xs:element name="bool2" type="glsl_bool2"/>
            <xs:element name="bool3" type="glsl_bool3"/>
            <xs:element name="bool4" type="glsl_bool4"/>
            <xs:element name="float" type="glsl_float"/>
            <xs:element name="float2" type="glsl_float2"/>
            <xs:element name="float3" type="glsl_float3"/>
            <xs:element name="float4" type="glsl_float4"/>
            <xs:element name="float2x2" type="glsl_float2x2"/>
            <xs:element name="float3x3" type="glsl_float3x3"/>
            <xs:element name="float4x4" type="glsl_float4x4"/>
            <xs:element name="int" type="glsl_int"/>
            <xs:element name="int2" type="glsl_int2"/>
            <xs:element name="int3" type="glsl_int3"/>
            <xs:element name="int4" type="glsl_int4"/>
            <xs:element name="surface" type="glsl_surface_type"/>
            <xs:element name="sampler1D" type="gl_sampler1D"/>
            <xs:element name="sampler2D" type="gl_sampler2D"/>
            <xs:element name="sampler3D" type="gl_sampler3D"/>
            <xs:element name="samplerCUBE" type="gl_samplerCUBE"/>
            <xs:element name="samplerRECT" type="gl_samplerRECT"/>
            <xs:element name="samplerDEPTH" type="gl_samplerDEPTH"/>
            <xs:element name="enum" type="gl_enumeration"/>
        </xs:choice>
    </xs:group>
    <xs:complexType name="glsl_newparam">
        <xs:sequence>
            <xs:element name="annotate" type="fx_annotate_common" minOccurs="0" maxOccurs="unbounded"/>
            <xs:element name="semantic" type="xs:NCName" minOccurs="0"/>
            <xs:element name="modifier" type="fx_modifier_enum_common" minOccurs="0"/>
            <xs:choice>
                <xs:group ref="glsl_param_type"/>
                <xs:element name="array" type="glsl_newarray_type"/>
            </xs:choice>
        </xs:sequence>
        <xs:attribute name="sid" type="glsl_identifier" use="required"/>
    </xs:complexType>
    <xs:complexType name="glsl_setparam_simple">
        <xs:sequence>
            <xs:element name="annotate" type="fx_annotate_common" minOccurs="0" maxOccurs="unbounded"/>
            <xs:group ref="glsl_param_type"/>
        </xs:sequence>
        <xs:attribute name="ref" type="glsl_identifier" use="required"/>
    </xs:complexType>
    <xs:complexType name="glsl_setparam">
        <xs:sequence>
            <xs:element name="annotate" type="fx_annotate_common" minOccurs="0" maxOccurs="unbounded"/>
            <xs:choice>
                <xs:group ref="glsl_param_type"/>
                <xs:element name="array" type="glsl_setarray_type"/>
            </xs:choice>
        </xs:sequence>
        <xs:attribute name="ref" type="glsl_identifier" use="required"/>
        <xs:attribute name="program" type="xs:NCName"/>
    </xs:complexType>
    <xs:element name="profile_GLSL" substitutionGroup="fx_profile_abstract">
        <xs:annotation>
            <xs:documentation>
            Opens a block of GLSL platform-specific data types and technique declarations.
            </xs:documentation>
        </xs:annotation>
        <xs:complexType>
            <xs:sequence>
                <xs:element ref="asset" minOccurs="0"/>
                <xs:choice minOccurs="0" maxOccurs="unbounded">
                    <xs:element name="code" type="fx_code_profile"/>
                    <xs:element name="include" type="fx_include_common"/>
                </xs:choice>
                <xs:choice minOccurs="0" maxOccurs="unbounded">
                    <xs:element ref="image"/>
                    <xs:element name="newparam" type="glsl_newparam"/>
                </xs:choice>
                <xs:element name="technique" maxOccurs="unbounded">
                    <xs:annotation>
                        <xs:documentation>
                        Holds a description of the textures, samplers, shaders, parameters, and passes necessary for rendering this effect using one method.
                        </xs:documentation>
                    </xs:annotation>
                    <xs:complexType>
                        <xs:sequence>
                            <xs:element name="annotate" type="fx_annotate_common" minOccurs="0" maxOccurs="unbounded"/>
                            <xs:choice minOccurs="0" maxOccurs="unbounded">
                                <xs:element name="code" type="fx_code_profile"/>
                                <xs:element name="include" type="fx_include_common"/>
                            </xs:choice>
                            <xs:choice minOccurs="0" maxOccurs="unbounded">
                                <xs:element ref="image"/>
                                <xs:element name="newparam" type="glsl_newparam"/>
                                <xs:element name="setparam" type="glsl_setparam"/>
                            </xs:choice>
                            <xs:element name="pass" maxOccurs="unbounded">
                                <xs:annotation>
                                    <xs:documentation>
                                    A static declaration of all the render states, shaders, and settings for one rendering pipeline.
                                    </xs:documentation>
                                </xs:annotation>
                                <xs:complexType>
                                    <xs:sequence>
                                        <xs:element name="annotate" type="fx_annotate_common" minOccurs="0" maxOccurs="unbounded"/>
                                        <xs:element name="color_target" type="fx_colortarget_common" minOccurs="0" maxOccurs="unbounded"/>
                                        <xs:element name="depth_target" type="fx_depthtarget_common" minOccurs="0" maxOccurs="unbounded"/>
                                        <xs:element name="stencil_target" type="fx_stenciltarget_common" minOccurs="0" maxOccurs="unbounded"/>
                                        <xs:element name="color_clear" type="fx_clearcolor_common" minOccurs="0" maxOccurs="unbounded"/>
                                        <xs:element name="depth_clear" type="fx_cleardepth_common" minOccurs="0" maxOccurs="unbounded"/>
                                        <xs:element name="stencil_clear" type="fx_clearstencil_common" minOccurs="0" maxOccurs="unbounded"/>
                                        <xs:element name="draw" type="fx_draw_common" minOccurs="0"/>
                                        <xs:choice maxOccurs="unbounded">
                                            <xs:group ref="gl_pipeline_settings"/>
                                            <xs:element name="shader">
                                                <xs:annotation>
                                                    <xs:documentation>
                                                    Declare and prepare a shader for execution in the rendering pipeline of a pass.
                                                    </xs:documentation>
                                                </xs:annotation>
                                                <xs:complexType>
                                                    <xs:sequence>
                                                        <xs:element name="annotate" type="fx_annotate_common" minOccurs="0" maxOccurs="unbounded"/>
                                                        <xs:sequence minOccurs="0">
                                                            <xs:element name="compiler_target">
                                                                <xs:annotation>
                                                                    <xs:documentation>
                                                                    A string declaring which profile or platform the compiler is targeting this shader for.
                                                                    </xs:documentation>
                                                                </xs:annotation>
                                                                <xs:complexType>
                                                                    <xs:simpleContent>
                                                                        <xs:extension base="xs:NMTOKEN"/>
                                                                    </xs:simpleContent>
                                                                </xs:complexType>
                                                            </xs:element>
                                                            <xs:element name="compiler_options" type="xs:string" minOccurs="0">
                                                                <xs:annotation>
                                                                    <xs:documentation>
                                                                    A string containing command-line operations for the shader compiler.
                                                                    </xs:documentation>
                                                                </xs:annotation>
                                                            </xs:element>
                                                        </xs:sequence>
                                                        <xs:element name="name">
                                                            <xs:annotation>
                                                                <xs:documentation>
                                                                The entry symbol for the shader function.
                                                                </xs:documentation>
                                                            </xs:annotation>
                                                            <xs:complexType>
                                                                <xs:simpleContent>
                                                                    <xs:extension base="xs:NCName">
                                                                        <xs:attribute name="source" type="xs:NCName" use="optional"/>
                                                                    </xs:extension>
                                                                </xs:simpleContent>
                                                            </xs:complexType>
                                                        </xs:element>
                                                        <xs:element name="bind" minOccurs="0" maxOccurs="unbounded">
                                                            <xs:annotation>
                                                                <xs:documentation>
                                                                Binds values to uniform inputs of a shader.
                                                                </xs:documentation>
                                                            </xs:annotation>
                                                            <xs:complexType>
                                                                <xs:choice>
                                                                    <xs:group ref="glsl_param_type"/>
                                                                    <xs:element name="param">
                                                                        <xs:complexType>
                                                                            <xs:attribute name="ref" type="xs:string" use="required"/>
                                                                        </xs:complexType>
                                                                    </xs:element>
                                                                </xs:choice>
                                                                <xs:attribute name="symbol" type="xs:NCName" use="required">
                                                                    <xs:annotation>
                                                                        <xs:documentation>
                                                                        The identifier for a uniform input parameter to the shader (a formal function parameter or in-scope
                                                                        global) that will be bound to an external resource.
                                                                        </xs:documentation>
                                                                    </xs:annotation>
                                                                </xs:attribute>
                                                            </xs:complexType>
                                                        </xs:element>
                                                    </xs:sequence>
                                                    <xs:attribute name="stage" type="glsl_pipeline_stage">
                                                        <xs:annotation>
                                                            <xs:documentation>
                                                            In which pipeline stage this programmable shader is designed to execute, for example, VERTEX, FRAGMENT, etc.
                                                            </xs:documentation>
                                                        </xs:annotation>
                                                    </xs:attribute>
                                                </xs:complexType>
                                            </xs:element>
                                        </xs:choice>
                                        <xs:element ref="extra" minOccurs="0" maxOccurs="unbounded"/>
                                    </xs:sequence>
                                    <xs:attribute name="sid" type="xs:NCName" use="optional">
                                        <xs:annotation>
                                            <xs:documentation>
                                            The sid attribute is a text string value containing the sub-identifier of this element.
                                            This value must be unique within the scope of the parent element. Optional attribute.
                                            </xs:documentation>
                                        </xs:annotation>
                                    </xs:attribute>
                                </xs:complexType>
                            </xs:element>
                            <xs:element ref="extra" minOccurs="0" maxOccurs="unbounded"/>
                        </xs:sequence>
                        <xs:attribute name="id" type="xs:ID">
                            <xs:annotation>
                                <xs:documentation>
                                The id attribute is a text string containing the unique identifier of this element.
                                This value must be unique within the instance document. Optional attribute.
                                </xs:documentation>
                            </xs:annotation>
                        </xs:attribute>
                        <xs:attribute name="sid" type="xs:NCName" use="required">
                            <xs:annotation>
                                <xs:documentation>
                                The sid attribute is a text string value containing the sub-identifier of this element.
                                This value must be unique within the scope of the parent element. Optional attribute.
                                </xs:documentation>
                            </xs:annotation>
                        </xs:attribute>
                    </xs:complexType>
                </xs:element>
                <xs:element ref="extra" minOccurs="0" maxOccurs="unbounded"/>
            </xs:sequence>
            <xs:attribute name="id" type="xs:ID" use="optional">
                <xs:annotation>
                    <xs:documentation>
                    The id attribute is a text string containing the unique identifier of this element.
                    This value must be unique within the instance document. Optional attribute.
                    </xs:documentation>
                </xs:annotation>
            </xs:attribute>
        </xs:complexType>
    </xs:element>
    <!-- =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-= -->
    <!-- COLLADA FX common profile                   -->
    <!-- =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-= -->
    <xs:complexType name="common_float_or_param_type">
        <xs:choice>
            <xs:element name="float">
                <xs:complexType>
                    <xs:simpleContent>
                        <xs:extension base="float">
                            <xs:attribute name="sid" type="xs:NCName"/>
                        </xs:extension>
                    </xs:simpleContent>
                </xs:complexType>
            </xs:element>
            <xs:element name="param">
                <xs:complexType>
                    <xs:attribute name="ref" type="xs:NCName" use="required"/>
                </xs:complexType>
            </xs:element>
        </xs:choice>
    </xs:complexType>
    <xs:complexType name="common_color_or_texture_type">
        <xs:choice>
            <xs:element name="color">
                <xs:complexType>
                    <xs:simpleContent>
                        <xs:extension base="fx_color_common">
                            <xs:attribute name="sid" type="xs:NCName"/>
                        </xs:extension>
                    </xs:simpleContent>
                </xs:complexType>
            </xs:element>
            <xs:element name="param">
                <xs:complexType>
                    <xs:attribute name="ref" type="xs:NCName" use="required"/>
                </xs:complexType>
            </xs:element>
            <xs:element name="texture">
                <xs:complexType>
                    <xs:sequence>
                        <xs:element ref="extra" minOccurs="0"/>
                    </xs:sequence>
                    <xs:attribute name="texture" type="xs:NCName" use="required"/>
                    <xs:attribute name="texcoord" type="xs:NCName" use="required"/>
                </xs:complexType>
            </xs:element>
        </xs:choice>
    </xs:complexType>
    <xs:complexType name="common_transparent_type">
        <xs:complexContent>
            <xs:extension base="common_color_or_texture_type">
                <xs:attribute name="opaque" type="fx_opaque_enum" default="A_ONE"/>
            </xs:extension>
        </xs:complexContent>
    </xs:complexType>
    <xs:complexType name="common_newparam_type">
        <xs:sequence>
            <xs:element name="semantic" type="xs:NCName" minOccurs="0"/>
            <xs:choice>
                <xs:element name="float" type="float"/>
                <xs:element name="float2" type="float2"/>
                <xs:element name="float3" type="float3"/>
                <xs:element name="float4" type="float4"/>
                <xs:element name="surface" type="fx_surface_common"/>
                <xs:element name="sampler2D" type="fx_sampler2D_common"/>
            </xs:choice>
        </xs:sequence>
        <xs:attribute name="sid" type="xs:NCName" use="required">
            <xs:annotation>
                <xs:documentation>
                The sid attribute is a text string value containing the sub-identifier of this element.
                This value must be unique within the scope of the parent element. Optional attribute.
                </xs:documentation>
            </xs:annotation>
        </xs:attribute>
    </xs:complexType>
    <xs:element name="profile_COMMON" substitutionGroup="fx_profile_abstract">
        <xs:annotation>
            <xs:documentation>
            Opens a block of COMMON platform-specific data types and technique declarations.
            </xs:documentation>
        </xs:annotation>
        <xs:complexType>
            <xs:sequence>
                <xs:element ref="asset" minOccurs="0"/>
                <xs:choice minOccurs="0" maxOccurs="unbounded">
                    <xs:element ref="image"/>
                    <xs:element name="newparam" type="common_newparam_type"/>
                </xs:choice>
                <xs:element name="technique">
                    <xs:annotation>
                        <xs:documentation>
                        Holds a description of the textures, samplers, shaders, parameters, and passes necessary for rendering this effect using one method.
                        </xs:documentation>
                    </xs:annotation>
                    <xs:complexType>
                        <xs:sequence>
                            <xs:element ref="asset" minOccurs="0">
                                <xs:annotation>
                                    <xs:documentation>
                                    The technique element may contain an asset element.
                                    </xs:documentation>
                                </xs:annotation>
                            </xs:element>
                            <xs:choice minOccurs="0" maxOccurs="unbounded">
                                <xs:element ref="image"/>
                                <xs:element name="newparam" type="common_newparam_type"/>
                            </xs:choice>
                            <xs:choice>
                                <xs:element name="constant">
                                    <xs:complexType>
                                        <xs:sequence>
                                            <xs:element name="emission" type="common_color_or_texture_type" minOccurs="0"/>
                                            <xs:element name="reflective" type="common_color_or_texture_type" minOccurs="0"/>
                                            <xs:element name="reflectivity" type="common_float_or_param_type" minOccurs="0"/>
                                            <xs:element name="transparent" type="common_transparent_type" minOccurs="0"/>
                                            <xs:element name="transparency" type="common_float_or_param_type" minOccurs="0"/>
                                            <xs:element name="index_of_refraction" type="common_float_or_param_type" minOccurs="0"/>
                                        </xs:sequence>
                                    </xs:complexType>
                                </xs:element>
                                <xs:element name="lambert">
                                    <xs:complexType>
                                        <xs:sequence>
                                            <xs:element name="emission" type="common_color_or_texture_type" minOccurs="0"/>
                                            <xs:element name="ambient" type="common_color_or_texture_type" minOccurs="0"/>
                                            <xs:element name="diffuse" type="common_color_or_texture_type" minOccurs="0"/>
                                            <xs:element name="reflective" type="common_color_or_texture_type" minOccurs="0"/>
                                            <xs:element name="reflectivity" type="common_float_or_param_type" minOccurs="0"/>
                                            <xs:element name="transparent" type="common_transparent_type" minOccurs="0"/>
                                            <xs:element name="transparency" type="common_float_or_param_type" minOccurs="0"/>
                                            <xs:element name="index_of_refraction" type="common_float_or_param_type" minOccurs="0"/>
                                        </xs:sequence>
                                    </xs:complexType>
                                </xs:element>
                                <xs:element name="phong">
                                    <xs:complexType>
                                        <xs:sequence>
                                            <xs:element name="emission" type="common_color_or_texture_type" minOccurs="0"/>
                                            <xs:element name="ambient" type="common_color_or_texture_type" minOccurs="0"/>
                                            <xs:element name="diffuse" type="common_color_or_texture_type" minOccurs="0"/>
                                            <xs:element name="specular" type="common_color_or_texture_type" minOccurs="0"/>
                                            <xs:element name="shininess" type="common_float_or_param_type" minOccurs="0"/>
                                            <xs:element name="reflective" type="common_color_or_texture_type" minOccurs="0"/>
                                            <xs:element name="reflectivity" type="common_float_or_param_type" minOccurs="0"/>
                                            <xs:element name="transparent" type="common_transparent_type" minOccurs="0"/>
                                            <xs:element name="transparency" type="common_float_or_param_type" minOccurs="0"/>
                                            <xs:element name="index_of_refraction" type="common_float_or_param_type" minOccurs="0"/>
                                    </xs:sequence>
                                    </xs:complexType>
                                </xs:element>
                                <xs:element name="blinn">
                                    <xs:complexType>
                                        <xs:sequence>
                                            <xs:element name="emission" type="common_color_or_texture_type" minOccurs="0"/>
                                            <xs:element name="ambient" type="common_color_or_texture_type" minOccurs="0"/>
                                            <xs:element name="diffuse" type="common_color_or_texture_type" minOccurs="0"/>
                                            <xs:element name="specular" type="common_color_or_texture_type" minOccurs="0"/>
                                            <xs:element name="shininess" type="common_float_or_param_type" minOccurs="0"/>
                                            <xs:element name="reflective" type="common_color_or_texture_type" minOccurs="0"/>
                                            <xs:element name="reflectivity" type="common_float_or_param_type" minOccurs="0"/>
                                            <xs:element name="transparent" type="common_transparent_type" minOccurs="0"/>
                                            <xs:element name="transparency" type="common_float_or_param_type" minOccurs="0"/>
                                            <xs:element name="index_of_refraction" type="common_float_or_param_type" minOccurs="0"/>
                                        </xs:sequence>
                                    </xs:complexType>
                                </xs:element>
                            </xs:choice>
                            <xs:element ref="extra" minOccurs="0" maxOccurs="unbounded">
                                <xs:annotation>
                                    <xs:documentation>
                                    The extra element may appear any number of times.
                                    </xs:documentation>
                                </xs:annotation>
                            </xs:element>
                        </xs:sequence>
                        <xs:attribute name="id" type="xs:ID">
                            <xs:annotation>
                                <xs:documentation>
                                The id attribute is a text string containing the unique identifier of this element.
                                This value must be unique within the instance document. Optional attribute.
                                </xs:documentation>
                            </xs:annotation>
                        </xs:attribute>
                        <xs:attribute name="sid" type="xs:NCName" use="required">
                            <xs:annotation>
                                <xs:documentation>
                                The sid attribute is a text string value containing the sub-identifier of this element.
                                This value must be unique within the scope of the parent element. Optional attribute.
                                </xs:documentation>
                            </xs:annotation>
                        </xs:attribute>
                    </xs:complexType>
                </xs:element>
                <xs:element ref="extra" minOccurs="0" maxOccurs="unbounded">
                    <xs:annotation>
                        <xs:documentation>
                        The extra element may appear any number of times.
                        </xs:documentation>
                    </xs:annotation>
                </xs:element>
            </xs:sequence>
            <xs:attribute name="id" type="xs:ID" use="optional">
                <xs:annotation>
                    <xs:documentation>
                    The id attribute is a text string containing the unique identifier of this element.
                    This value must be unique within the instance document. Optional attribute.
                    </xs:documentation>
                </xs:annotation>
            </xs:attribute>
        </xs:complexType>
    </xs:element>
    <!-- =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-= -->
    <!-- COLLADA FX Cg elements                      -->
    <!-- =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-= -->
    <xs:simpleType name="cg_bool">
        <xs:restriction base="xs:boolean"/>
    </xs:simpleType>
    <xs:simpleType name="cg_float">
        <xs:restriction base="xs:float"/>
    </xs:simpleType>
    <xs:simpleType name="cg_int">
        <xs:restriction base="xs:int"/>
    </xs:simpleType>
    <xs:simpleType name="cg_half">
        <xs:restriction base="xs:float"/>
    </xs:simpleType>
    <xs:simpleType name="cg_fixed">
        <xs:restriction base="xs:float">
            <xs:minInclusive value="-2.0"/>
            <xs:maxInclusive value="2.0"/>
            <!-- as defined for fp30 profile -->
        </xs:restriction>
    </xs:simpleType>
    <xs:simpleType name="cg_bool1">
        <xs:restriction base="xs:boolean"/>
    </xs:simpleType>
    <xs:simpleType name="cg_float1">
        <xs:restriction base="xs:float"/>
    </xs:simpleType>
    <xs:simpleType name="cg_int1">
        <xs:restriction base="xs:int"/>
    </xs:simpleType>
    <xs:simpleType name="cg_half1">
        <xs:restriction base="xs:float"/>
    </xs:simpleType>
    <xs:simpleType name="cg_fixed1">
        <xs:restriction base="xs:float">
            <xs:minInclusive value="-2.0"/>
            <xs:maxInclusive value="2.0"/>
            <!-- as defined for fp30 profile -->
        </xs:restriction>
    </xs:simpleType>
    <xs:simpleType name="cg_ListOfBool">
        <xs:list itemType="cg_bool"/>
    </xs:simpleType>
    <xs:simpleType name="cg_ListOfFloat">
        <xs:list itemType="cg_float"/>
    </xs:simpleType>
    <xs:simpleType name="cg_ListOfInt">
        <xs:list itemType="cg_int"/>
    </xs:simpleType>
    <xs:simpleType name="cg_ListOfHalf">
        <xs:list itemType="cg_half"/>
    </xs:simpleType>
    <xs:simpleType name="cg_ListOfFixed">
        <xs:list itemType="cg_fixed"/>
    </xs:simpleType>
    <xs:simpleType name="cg_bool2">
        <xs:restriction base="cg_ListOfBool">
            <xs:minLength value="2"/>
            <xs:maxLength value="2"/>
        </xs:restriction>
    </xs:simpleType>
    <xs:simpleType name="cg_bool3">
        <xs:restriction base="cg_ListOfBool">
            <xs:minLength value="3"/>
            <xs:maxLength value="3"/>
        </xs:restriction>
    </xs:simpleType>
    <xs:simpleType name="cg_bool4">
        <xs:restriction base="cg_ListOfBool">
            <xs:minLength value="4"/>
            <xs:maxLength value="4"/>
        </xs:restriction>
    </xs:simpleType>
    <xs:simpleType name="cg_bool1x1">
        <xs:restriction base="cg_ListOfBool">
            <xs:minLength value="1"/>
            <xs:maxLength value="1"/>
        </xs:restriction>
    </xs:simpleType>
    <xs:simpleType name="cg_bool1x2">
        <xs:restriction base="cg_ListOfBool">
            <xs:minLength value="2"/>
            <xs:maxLength value="2"/>
        </xs:restriction>
    </xs:simpleType>
    <xs:simpleType name="cg_bool1x3">
        <xs:restriction base="cg_ListOfBool">
            <xs:minLength value="3"/>
            <xs:maxLength value="3"/>
        </xs:restriction>
    </xs:simpleType>
    <xs:simpleType name="cg_bool1x4">
        <xs:restriction base="cg_ListOfBool">
            <xs:minLength value="4"/>
            <xs:maxLength value="4"/>
        </xs:restriction>
    </xs:simpleType>
    <xs:simpleType name="cg_bool2x1">
        <xs:restriction base="cg_ListOfBool">
            <xs:minLength value="2"/>
            <xs:maxLength value="2"/>
        </xs:restriction>
    </xs:simpleType>
    <xs:simpleType name="cg_bool2x2">
        <xs:restriction base="cg_ListOfBool">
            <xs:minLength value="4"/>
            <xs:maxLength value="4"/>
        </xs:restriction>
    </xs:simpleType>
    <xs:simpleType name="cg_bool2x3">
        <xs:restriction base="cg_ListOfBool">
            <xs:minLength value="6"/>
            <xs:maxLength value="6"/>
        </xs:restriction>
    </xs:simpleType>
    <xs:simpleType name="cg_bool2x4">
        <xs:restriction base="cg_ListOfBool">
            <xs:minLength value="8"/>
            <xs:maxLength value="8"/>
        </xs:restriction>
    </xs:simpleType>
    <xs:simpleType name="cg_bool3x1">
        <xs:restriction base="cg_ListOfBool">
            <xs:minLength value="3"/>
            <xs:maxLength value="3"/>
        </xs:restriction>
    </xs:simpleType>
    <xs:simpleType name="cg_bool3x2">
        <xs:restriction base="cg_ListOfBool">
            <xs:minLength value="6"/>
            <xs:maxLength value="6"/>
        </xs:restriction>
    </xs:simpleType>
    <xs:simpleType name="cg_bool3x3">
        <xs:restriction base="cg_ListOfBool">
            <xs:minLength value="9"/>
            <xs:maxLength value="9"/>
        </xs:restriction>
    </xs:simpleType>
    <xs:simpleType name="cg_bool3x4">
        <xs:restriction base="cg_ListOfBool">
            <xs:minLength value="12"/>
            <xs:maxLength value="12"/>
        </xs:restriction>
    </xs:simpleType>
    <xs:simpleType name="cg_bool4x1">
        <xs:restriction base="cg_ListOfBool">
            <xs:minLength value="4"/>
            <xs:maxLength value="4"/>
        </xs:restriction>
    </xs:simpleType>
    <xs:simpleType name="cg_bool4x2">
        <xs:restriction base="cg_ListOfBool">
            <xs:minLength value="8"/>
            <xs:maxLength value="8"/>
        </xs:restriction>
    </xs:simpleType>
    <xs:simpleType name="cg_bool4x3">
        <xs:restriction base="cg_ListOfBool">
            <xs:minLength value="12"/>
            <xs:maxLength value="12"/>
        </xs:restriction>
    </xs:simpleType>
    <xs:simpleType name="cg_bool4x4">
        <xs:restriction base="cg_ListOfBool">
            <xs:minLength value="16"/>
            <xs:maxLength value="16"/>
        </xs:restriction>
    </xs:simpleType>
    <xs:simpleType name="cg_float2">
        <xs:restriction base="cg_ListOfFloat">
            <xs:minLength value="2"/>
            <xs:maxLength value="2"/>
        </xs:restriction>
    </xs:simpleType>
    <xs:simpleType name="cg_float3">
        <xs:restriction base="cg_ListOfFloat">
            <xs:minLength value="3"/>
            <xs:maxLength value="3"/>
        </xs:restriction>
    </xs:simpleType>
    <xs:simpleType name="cg_float4">
        <xs:restriction base="cg_ListOfFloat">
            <xs:minLength value="4"/>
            <xs:maxLength value="4"/>
        </xs:restriction>
    </xs:simpleType>
    <xs:simpleType name="cg_float1x1">
        <xs:restriction base="cg_ListOfFloat">
            <xs:minLength value="1"/>
            <xs:maxLength value="1"/>
        </xs:restriction>
    </xs:simpleType>
    <xs:simpleType name="cg_float1x2">
        <xs:restriction base="cg_ListOfFloat">
            <xs:minLength value="2"/>
            <xs:maxLength value="2"/>
        </xs:restriction>
    </xs:simpleType>
    <xs:simpleType name="cg_float1x3">
        <xs:restriction base="cg_ListOfFloat">
            <xs:minLength value="3"/>
            <xs:maxLength value="3"/>
        </xs:restriction>
    </xs:simpleType>
    <xs:simpleType name="cg_float1x4">
        <xs:restriction base="cg_ListOfFloat">
            <xs:minLength value="4"/>
            <xs:maxLength value="4"/>
        </xs:restriction>
    </xs:simpleType>
    <xs:simpleType name="cg_float2x1">
        <xs:restriction base="cg_ListOfFloat">
            <xs:minLength value="2"/>
            <xs:maxLength value="2"/>
        </xs:restriction>
    </xs:simpleType>
    <xs:simpleType name="cg_float2x2">
        <xs:restriction base="cg_ListOfFloat">
            <xs:minLength value="4"/>
            <xs:maxLength value="4"/>
        </xs:restriction>
    </xs:simpleType>
    <xs:simpleType name="cg_float2x3">
        <xs:restriction base="cg_ListOfFloat">
            <xs:minLength value="6"/>
            <xs:maxLength value="6"/>
        </xs:restriction>
    </xs:simpleType>
    <xs:simpleType name="cg_float2x4">
        <xs:restriction base="cg_ListOfFloat">
            <xs:minLength value="8"/>
            <xs:maxLength value="8"/>
        </xs:restriction>
    </xs:simpleType>
    <xs:simpleType name="cg_float3x1">
        <xs:restriction base="cg_ListOfFloat">
            <xs:minLength value="3"/>
            <xs:maxLength value="3"/>
        </xs:restriction>
    </xs:simpleType>
    <xs:simpleType name="cg_float3x2">
        <xs:restriction base="cg_ListOfFloat">
            <xs:minLength value="6"/>
            <xs:maxLength value="6"/>
        </xs:restriction>
    </xs:simpleType>
    <xs:simpleType name="cg_float3x3">
        <xs:restriction base="cg_ListOfFloat">
            <xs:minLength value="9"/>
            <xs:maxLength value="9"/>
        </xs:restriction>
    </xs:simpleType>
    <xs:simpleType name="cg_float3x4">
        <xs:restriction base="cg_ListOfFloat">
            <xs:minLength value="12"/>
            <xs:maxLength value="12"/>
        </xs:restriction>
    </xs:simpleType>
    <xs:simpleType name="cg_float4x1">
        <xs:restriction base="cg_ListOfFloat">
            <xs:minLength value="4"/>
            <xs:maxLength value="4"/>
        </xs:restriction>
    </xs:simpleType>
    <xs:simpleType name="cg_float4x2">
        <xs:restriction base="cg_ListOfFloat">
            <xs:minLength value="8"/>
            <xs:maxLength value="8"/>
        </xs:restriction>
    </xs:simpleType>
    <xs:simpleType name="cg_float4x3">
        <xs:restriction base="cg_ListOfFloat">
            <xs:minLength value="12"/>
            <xs:maxLength value="12"/>
        </xs:restriction>
    </xs:simpleType>
    <xs:simpleType name="cg_float4x4">
        <xs:restriction base="cg_ListOfFloat">
            <xs:minLength value="16"/>
            <xs:maxLength value="16"/>
        </xs:restriction>
    </xs:simpleType>
    <xs:simpleType name="cg_int2">
        <xs:restriction base="cg_ListOfInt">
            <xs:minLength value="2"/>
            <xs:maxLength value="2"/>
        </xs:restriction>
    </xs:simpleType>
    <xs:simpleType name="cg_int3">
        <xs:restriction base="cg_ListOfInt">
            <xs:minLength value="3"/>
            <xs:maxLength value="3"/>
        </xs:restriction>
    </xs:simpleType>
    <xs:simpleType name="cg_int4">
        <xs:restriction base="cg_ListOfInt">
            <xs:minLength value="4"/>
            <xs:maxLength value="4"/>
        </xs:restriction>
    </xs:simpleType>
    <xs:simpleType name="cg_int1x1">
        <xs:restriction base="cg_ListOfInt">
            <xs:minLength value="1"/>
            <xs:maxLength value="1"/>
        </xs:restriction>
    </xs:simpleType>
    <xs:simpleType name="cg_int1x2">
        <xs:restriction base="cg_ListOfInt">
            <xs:minLength value="2"/>
            <xs:maxLength value="2"/>
        </xs:restriction>
    </xs:simpleType>
    <xs:simpleType name="cg_int1x3">
        <xs:restriction base="cg_ListOfInt">
            <xs:minLength value="3"/>
            <xs:maxLength value="3"/>
        </xs:restriction>
    </xs:simpleType>
    <xs:simpleType name="cg_int1x4">
        <xs:restriction base="cg_ListOfInt">
            <xs:minLength value="4"/>
            <xs:maxLength value="4"/>
        </xs:restriction>
    </xs:simpleType>
    <xs:simpleType name="cg_int2x1">
        <xs:restriction base="cg_ListOfInt">
            <xs:minLength value="2"/>
            <xs:maxLength value="2"/>
        </xs:restriction>
    </xs:simpleType>
    <xs:simpleType name="cg_int2x2">
        <xs:restriction base="cg_ListOfInt">
            <xs:minLength value="4"/>
            <xs:maxLength value="4"/>
        </xs:restriction>
    </xs:simpleType>
    <xs:simpleType name="cg_int2x3">
        <xs:restriction base="cg_ListOfInt">
            <xs:minLength value="6"/>
            <xs:maxLength value="6"/>
        </xs:restriction>
    </xs:simpleType>
    <xs:simpleType name="cg_int2x4">
        <xs:restriction base="cg_ListOfInt">
            <xs:minLength value="8"/>
            <xs:maxLength value="8"/>
        </xs:restriction>
    </xs:simpleType>
    <xs:simpleType name="cg_int3x1">
        <xs:restriction base="cg_ListOfInt">
            <xs:minLength value="3"/>
            <xs:maxLength value="3"/>
        </xs:restriction>
    </xs:simpleType>
    <xs:simpleType name="cg_int3x2">
        <xs:restriction base="cg_ListOfInt">
            <xs:minLength value="6"/>
            <xs:maxLength value="6"/>
        </xs:restriction>
    </xs:simpleType>
    <xs:simpleType name="cg_int3x3">
        <xs:restriction base="cg_ListOfInt">
            <xs:minLength value="9"/>
            <xs:maxLength value="9"/>
        </xs:restriction>
    </xs:simpleType>
    <xs:simpleType name="cg_int3x4">
        <xs:restriction base="cg_ListOfInt">
            <xs:minLength value="12"/>
            <xs:maxLength value="12"/>
        </xs:restriction>
    </xs:simpleType>
    <xs:simpleType name="cg_int4x1">
        <xs:restriction base="cg_ListOfInt">
            <xs:minLength value="4"/>
            <xs:maxLength value="4"/>
        </xs:restriction>
    </xs:simpleType>
    <xs:simpleType name="cg_int4x2">
        <xs:restriction base="cg_ListOfInt">
            <xs:minLength value="8"/>
            <xs:maxLength value="8"/>
        </xs:restriction>
    </xs:simpleType>
    <xs:simpleType name="cg_int4x3">
        <xs:restriction base="cg_ListOfInt">
            <xs:minLength value="12"/>
            <xs:maxLength value="12"/>
        </xs:restriction>
    </xs:simpleType>
    <xs:simpleType name="cg_int4x4">
        <xs:restriction base="cg_ListOfInt">
            <xs:minLength value="16"/>
            <xs:maxLength value="16"/>
        </xs:restriction>
    </xs:simpleType>
    <xs:simpleType name="cg_half2">
        <xs:restriction base="cg_ListOfHalf">
            <xs:minLength value="2"/>
            <xs:maxLength value="2"/>
        </xs:restriction>
    </xs:simpleType>
    <xs:simpleType name="cg_half3">
        <xs:restriction base="cg_ListOfHalf">
            <xs:minLength value="3"/>
            <xs:maxLength value="3"/>
        </xs:restriction>
    </xs:simpleType>
    <xs:simpleType name="cg_half4">
        <xs:restriction base="cg_ListOfHalf">
            <xs:minLength value="4"/>
            <xs:maxLength value="4"/>
        </xs:restriction>
    </xs:simpleType>
    <xs:simpleType name="cg_half1x1">
        <xs:restriction base="cg_ListOfHalf">
            <xs:minLength value="1"/>
            <xs:maxLength value="1"/>
        </xs:restriction>
    </xs:simpleType>
    <xs:simpleType name="cg_half1x2">
        <xs:restriction base="cg_ListOfHalf">
            <xs:minLength value="2"/>
            <xs:maxLength value="2"/>
        </xs:restriction>
    </xs:simpleType>
    <xs:simpleType name="cg_half1x3">
        <xs:restriction base="cg_ListOfHalf">
            <xs:minLength value="3"/>
            <xs:maxLength value="3"/>
        </xs:restriction>
    </xs:simpleType>
    <xs:simpleType name="cg_half1x4">
        <xs:restriction base="cg_ListOfHalf">
            <xs:minLength value="4"/>
            <xs:maxLength value="4"/>
        </xs:restriction>
    </xs:simpleType>
    <xs:simpleType name="cg_half2x1">
        <xs:restriction base="cg_ListOfHalf">
            <xs:minLength value="2"/>
            <xs:maxLength value="2"/>
        </xs:restriction>
    </xs:simpleType>
    <xs:simpleType name="cg_half2x2">
        <xs:restriction base="cg_ListOfHalf">
            <xs:minLength value="4"/>
            <xs:maxLength value="4"/>
        </xs:restriction>
    </xs:simpleType>
    <xs:simpleType name="cg_half2x3">
        <xs:restriction base="cg_ListOfHalf">
            <xs:minLength value="6"/>
            <xs:maxLength value="6"/>
        </xs:restriction>
    </xs:simpleType>
    <xs:simpleType name="cg_half2x4">
        <xs:restriction base="cg_ListOfHalf">
            <xs:minLength value="8"/>
            <xs:maxLength value="8"/>
        </xs:restriction>
    </xs:simpleType>
    <xs:simpleType name="cg_half3x1">
        <xs:restriction base="cg_ListOfHalf">
            <xs:minLength value="3"/>
            <xs:maxLength value="3"/>
        </xs:restriction>
    </xs:simpleType>
    <xs:simpleType name="cg_half3x2">
        <xs:restriction base="cg_ListOfHalf">
            <xs:minLength value="6"/>
            <xs:maxLength value="6"/>
        </xs:restriction>
    </xs:simpleType>
    <xs:simpleType name="cg_half3x3">
        <xs:restriction base="cg_ListOfHalf">
            <xs:minLength value="9"/>
            <xs:maxLength value="9"/>
        </xs:restriction>
    </xs:simpleType>
    <xs:simpleType name="cg_half3x4">
        <xs:restriction base="cg_ListOfHalf">
            <xs:minLength value="12"/>
            <xs:maxLength value="12"/>
        </xs:restriction>
    </xs:simpleType>
    <xs:simpleType name="cg_half4x1">
        <xs:restriction base="cg_ListOfHalf">
            <xs:minLength value="4"/>
            <xs:maxLength value="4"/>
        </xs:restriction>
    </xs:simpleType>
    <xs:simpleType name="cg_half4x2">
        <xs:restriction base="cg_ListOfHalf">
            <xs:minLength value="8"/>
            <xs:maxLength value="8"/>
        </xs:restriction>
    </xs:simpleType>
    <xs:simpleType name="cg_half4x3">
        <xs:restriction base="cg_ListOfHalf">
            <xs:minLength value="12"/>
            <xs:maxLength value="12"/>
        </xs:restriction>
    </xs:simpleType>
    <xs:simpleType name="cg_half4x4">
        <xs:restriction base="cg_ListOfHalf">
            <xs:minLength value="16"/>
            <xs:maxLength value="16"/>
        </xs:restriction>
    </xs:simpleType>
    <xs:simpleType name="cg_fixed2">
        <xs:restriction base="cg_ListOfFixed">
            <xs:minLength value="2"/>
            <xs:maxLength value="2"/>
        </xs:restriction>
    </xs:simpleType>
    <xs:simpleType name="cg_fixed3">
        <xs:restriction base="cg_ListOfFixed">
            <xs:minLength value="3"/>
            <xs:maxLength value="3"/>
        </xs:restriction>
    </xs:simpleType>
    <xs:simpleType name="cg_fixed4">
        <xs:restriction base="cg_ListOfFixed">
            <xs:minLength value="4"/>
            <xs:maxLength value="4"/>
        </xs:restriction>
    </xs:simpleType>
    <xs:simpleType name="cg_fixed1x1">
        <xs:restriction base="cg_ListOfFixed">
            <xs:minLength value="1"/>
            <xs:maxLength value="1"/>
        </xs:restriction>
    </xs:simpleType>
    <xs:simpleType name="cg_fixed1x2">
        <xs:restriction base="cg_ListOfFixed">
            <xs:minLength value="2"/>
            <xs:maxLength value="2"/>
        </xs:restriction>
    </xs:simpleType>
    <xs:simpleType name="cg_fixed1x3">
        <xs:restriction base="cg_ListOfFixed">
            <xs:minLength value="3"/>
            <xs:maxLength value="3"/>
        </xs:restriction>
    </xs:simpleType>
    <xs:simpleType name="cg_fixed1x4">
        <xs:restriction base="cg_ListOfFixed">
            <xs:minLength value="4"/>
            <xs:maxLength value="4"/>
        </xs:restriction>
    </xs:simpleType>
    <xs:simpleType name="cg_fixed2x1">
        <xs:restriction base="cg_ListOfFixed">
            <xs:minLength value="2"/>
            <xs:maxLength value="2"/>
        </xs:restriction>
    </xs:simpleType>
    <xs:simpleType name="cg_fixed2x2">
        <xs:restriction base="cg_ListOfFixed">
            <xs:minLength value="4"/>
            <xs:maxLength value="4"/>
        </xs:restriction>
    </xs:simpleType>
    <xs:simpleType name="cg_fixed2x3">
        <xs:restriction base="cg_ListOfFixed">
            <xs:minLength value="6"/>
            <xs:maxLength value="6"/>
        </xs:restriction>
    </xs:simpleType>
    <xs:simpleType name="cg_fixed2x4">
        <xs:restriction base="cg_ListOfFixed">
            <xs:minLength value="8"/>
            <xs:maxLength value="8"/>
        </xs:restriction>
    </xs:simpleType>
    <xs:simpleType name="cg_fixed3x1">
        <xs:restriction base="cg_ListOfFixed">
            <xs:minLength value="3"/>
            <xs:maxLength value="3"/>
        </xs:restriction>
    </xs:simpleType>
    <xs:simpleType name="cg_fixed3x2">
        <xs:restriction base="cg_ListOfFixed">
            <xs:minLength value="6"/>
            <xs:maxLength value="6"/>
        </xs:restriction>
    </xs:simpleType>
    <xs:simpleType name="cg_fixed3x3">
        <xs:restriction base="cg_ListOfFixed">
            <xs:minLength value="9"/>
            <xs:maxLength value="9"/>
        </xs:restriction>
    </xs:simpleType>
    <xs:simpleType name="cg_fixed3x4">
        <xs:restriction base="cg_ListOfFixed">
            <xs:minLength value="12"/>
            <xs:maxLength value="12"/>
        </xs:restriction>
    </xs:simpleType>
    <xs:simpleType name="cg_fixed4x1">
        <xs:restriction base="cg_ListOfFixed">
            <xs:minLength value="4"/>
            <xs:maxLength value="4"/>
        </xs:restriction>
    </xs:simpleType>
    <xs:simpleType name="cg_fixed4x2">
        <xs:restriction base="cg_ListOfFixed">
            <xs:minLength value="8"/>
            <xs:maxLength value="8"/>
        </xs:restriction>
    </xs:simpleType>
    <xs:simpleType name="cg_fixed4x3">
        <xs:restriction base="cg_ListOfFixed">
            <xs:minLength value="12"/>
            <xs:maxLength value="12"/>
        </xs:restriction>
    </xs:simpleType>
    <xs:simpleType name="cg_fixed4x4">
        <xs:restriction base="cg_ListOfFixed">
            <xs:minLength value="16"/>
            <xs:maxLength value="16"/>
        </xs:restriction>
    </xs:simpleType>
    <xs:complexType name="cg_sampler1D">
        <xs:complexContent>
            <xs:extension base="fx_sampler1D_common"/>
        </xs:complexContent>
    </xs:complexType>
    <xs:complexType name="cg_sampler2D">
        <xs:complexContent>
            <xs:extension base="fx_sampler2D_common"/>
        </xs:complexContent>
    </xs:complexType>
    <xs:complexType name="cg_sampler3D">
        <xs:complexContent>
            <xs:extension base="fx_sampler3D_common"/>
        </xs:complexContent>
    </xs:complexType>
    <xs:complexType name="cg_samplerCUBE">
        <xs:complexContent>
            <xs:extension base="fx_samplerCUBE_common"/>
        </xs:complexContent>
    </xs:complexType>
    <xs:complexType name="cg_samplerRECT">
        <xs:complexContent>
            <xs:extension base="fx_samplerRECT_common"/>
        </xs:complexContent>
    </xs:complexType>
    <xs:complexType name="cg_samplerDEPTH">
        <xs:complexContent>
            <xs:extension base="fx_samplerDEPTH_common"/>
        </xs:complexContent>
    </xs:complexType>
    <xs:simpleType name="cg_pipeline_stage">
        <xs:restriction base="xs:string">
            <xs:enumeration value="VERTEX"/>
            <xs:enumeration value="FRAGMENT"/>
        </xs:restriction>
    </xs:simpleType>
    <xs:simpleType name="cg_identifier">
        <xs:restriction base="xs:token"/>
        <!-- type used to represent identifiers in Cg, e.g. "myLight.bitmap[2].width" -->
    </xs:simpleType>
    <xs:complexType name="cg_connect_param">
        <xs:annotation>
            <xs:documentation>
            Creates a symbolic connection between two previously defined parameters.
            </xs:documentation>
        </xs:annotation>
        <xs:attribute name="ref" type="cg_identifier" use="required"/>
    </xs:complexType>
    <xs:complexType name="cg_newarray_type">
        <xs:annotation>
            <xs:documentation>
            Creates a parameter of a one-dimensional array type.
            </xs:documentation>
        </xs:annotation>
        <xs:choice minOccurs="0" maxOccurs="unbounded">
            <xs:group ref="cg_param_type"/>
            <xs:element name="array" type="cg_newarray_type">
                <xs:annotation>
                    <xs:documentation>
                    Nested array elements allow you to create multidemensional arrays.
                    </xs:documentation>
                </xs:annotation>
            </xs:element>
            <xs:element name="usertype" type="cg_setuser_type">
                <xs:annotation>
                    <xs:documentation>
                    The usertype element allows you to create arrays of usertypes.
                    </xs:documentation>
                </xs:annotation>
            </xs:element>
            <xs:element name="connect_param" type="cg_connect_param"/>
        </xs:choice>
        <xs:attribute name="length" type="xs:positiveInteger" use="required">
            <xs:annotation>
                <xs:documentation>
                The length attribute specifies the length of the array.
                </xs:documentation>
            </xs:annotation>
        </xs:attribute>
    </xs:complexType>
    <xs:complexType name="cg_setarray_type">
        <xs:annotation>
            <xs:documentation>
            Creates a parameter of a one-dimensional array type.
            </xs:documentation>
        </xs:annotation>
        <xs:choice minOccurs="0" maxOccurs="unbounded">
            <xs:group ref="cg_param_type"/>
            <xs:element name="array" type="cg_setarray_type">
                <xs:annotation>
                    <xs:documentation>
                    Nested array elements allow you to create multidemensional arrays.
                    </xs:documentation>
                </xs:annotation>
            </xs:element>
            <xs:element name="usertype" type="cg_setuser_type">
                <xs:annotation>
                    <xs:documentation>
                    The usertype element allows you to create arrays of usertypes.
                    </xs:documentation>
                </xs:annotation>
            </xs:element>
        </xs:choice>
        <xs:attribute name="length" type="xs:positiveInteger" use="optional">
            <xs:annotation>
                <xs:documentation>
                The length attribute specifies the length of the array.
                </xs:documentation>
            </xs:annotation>
        </xs:attribute>
    </xs:complexType>
    <xs:complexType name="cg_setuser_type">
        <xs:annotation>
            <xs:documentation>
            Creates an instance of a structured class.
            </xs:documentation>
        </xs:annotation>
        <xs:choice minOccurs="0">
            <xs:annotation>
                <xs:documentation>Some usertypes do not have data.  They may be used only to implement interface functions.</xs:documentation>
            </xs:annotation>
            <xs:choice maxOccurs="unbounded">
                <xs:annotation>
                    <xs:documentation>Use a combination of these to initialize the usertype in an order-dependent manner.</xs:documentation>
                </xs:annotation>
                <xs:group ref="cg_param_type"/>
                <xs:element name="array" type="cg_setarray_type"/>
                <xs:element name="usertype" type="cg_setuser_type"/>
                <xs:element name="connect_param" type="cg_connect_param"/>
            </xs:choice>
            <xs:element name="setparam" type="cg_setparam" maxOccurs="unbounded">
                <xs:annotation>
                    <xs:documentation>Use a series of these to set the members by name.  The ref attribute will be relative to the usertype you are in right now.</xs:documentation>
                </xs:annotation>
            </xs:element>
        </xs:choice>
        <xs:attribute name="name" type="cg_identifier" use="required"/>
        <xs:attribute name="source" type="xs:NCName" use="required">
            <xs:annotation>
                <xs:documentation>
                    Reference a code or include element which defines the usertype
                </xs:documentation>
            </xs:annotation>
        </xs:attribute>
    </xs:complexType>
    <xs:complexType name="cg_surface_type">
        <xs:annotation>
            <xs:documentation>
            Declares a resource that can be used both as the source for texture samples and as the target of a rendering pass.
            </xs:documentation>
        </xs:annotation>
        <xs:complexContent>
            <xs:extension base="fx_surface_common">
                <xs:sequence>
                    <xs:element name="generator" minOccurs="0">
                        <xs:annotation>
                            <xs:documentation>
                            A procedural surface generator for the cg profile.
                            </xs:documentation>
                        </xs:annotation>
                        <xs:complexType>
                            <xs:sequence>
                                <xs:element name="annotate" type="fx_annotate_common" minOccurs="0" maxOccurs="unbounded">
                                    <xs:annotation>
                                        <xs:documentation>
                                        The annotate element allows you to specify an annotation for this generator.
                                        </xs:documentation>
                                    </xs:annotation>
                                </xs:element>
                                <xs:choice maxOccurs="unbounded">
                                    <xs:element name="code" type="fx_code_profile">
                                        <xs:annotation>
                                            <xs:documentation>
                                            The code element allows you to embed cg sourcecode for the surface generator.
                                            </xs:documentation>
                                        </xs:annotation>
                                    </xs:element>
                                    <xs:element name="include" type="fx_include_common">
                                        <xs:annotation>
                                            <xs:documentation>
                                            The include element imports cg source code or precompiled binary shaders into the FX Runtime by referencing an external resource.
                                            </xs:documentation>
                                        </xs:annotation>
                                    </xs:element>
                                </xs:choice>
                                <xs:element name="name">
                                    <xs:annotation>
                                        <xs:documentation>
                                        The entry symbol for the shader function.
                                        </xs:documentation>
                                    </xs:annotation>
                                    <xs:complexType>
                                        <xs:simpleContent>
                                            <xs:extension base="xs:NCName">
                                                <xs:attribute name="source" type="xs:NCName" use="optional"/>
                                            </xs:extension>
                                        </xs:simpleContent>
                                    </xs:complexType>
                                </xs:element>
                                <xs:element name="setparam" type="cg_setparam_simple" minOccurs="0" maxOccurs="unbounded">
                                    <xs:annotation>
                                        <xs:documentation>
                                            Assigns a new value to a previously defined parameter.
                                        </xs:documentation>
                                    </xs:annotation>
                                </xs:element>
                            </xs:sequence>
                        </xs:complexType>
                    </xs:element>
                </xs:sequence>
            </xs:extension>
        </xs:complexContent>
    </xs:complexType>
    <xs:group name="cg_param_type">
        <xs:annotation>
            <xs:documentation>
            A group that specifies the allowable types for CG profile parameters.
            </xs:documentation>
        </xs:annotation>
        <xs:choice>
            <xs:element name="bool" type="cg_bool"/>
            <xs:element name="bool1" type="cg_bool1"/>
            <xs:element name="bool2" type="cg_bool2"/>
            <xs:element name="bool3" type="cg_bool3"/>
            <xs:element name="bool4" type="cg_bool4"/>
            <xs:element name="bool1x1" type="cg_bool1x1"/>
            <xs:element name="bool1x2" type="cg_bool1x2"/>
            <xs:element name="bool1x3" type="cg_bool1x3"/>
            <xs:element name="bool1x4" type="cg_bool1x4"/>
            <xs:element name="bool2x1" type="cg_bool2x1"/>
            <xs:element name="bool2x2" type="cg_bool2x2"/>
            <xs:element name="bool2x3" type="cg_bool2x3"/>
            <xs:element name="bool2x4" type="cg_bool2x4"/>
            <xs:element name="bool3x1" type="cg_bool3x1"/>
            <xs:element name="bool3x2" type="cg_bool3x2"/>
            <xs:element name="bool3x3" type="cg_bool3x3"/>
            <xs:element name="bool3x4" type="cg_bool3x4"/>
            <xs:element name="bool4x1" type="cg_bool4x1"/>
            <xs:element name="bool4x2" type="cg_bool4x2"/>
            <xs:element name="bool4x3" type="cg_bool4x3"/>
            <xs:element name="bool4x4" type="cg_bool4x4"/>
            <xs:element name="float" type="cg_float"/>
            <xs:element name="float1" type="cg_float1"/>
            <xs:element name="float2" type="cg_float2"/>
            <xs:element name="float3" type="cg_float3"/>
            <xs:element name="float4" type="cg_float4"/>
            <xs:element name="float1x1" type="cg_float1x1"/>
            <xs:element name="float1x2" type="cg_float1x2"/>
            <xs:element name="float1x3" type="cg_float1x3"/>
            <xs:element name="float1x4" type="cg_float1x4"/>
            <xs:element name="float2x1" type="cg_float2x1"/>
            <xs:element name="float2x2" type="cg_float2x2"/>
            <xs:element name="float2x3" type="cg_float2x3"/>
            <xs:element name="float2x4" type="cg_float2x4"/>
            <xs:element name="float3x1" type="cg_float3x1"/>
            <xs:element name="float3x2" type="cg_float3x2"/>
            <xs:element name="float3x3" type="cg_float3x3"/>
            <xs:element name="float3x4" type="cg_float3x4"/>
            <xs:element name="float4x1" type="cg_float4x1"/>
            <xs:element name="float4x2" type="cg_float4x2"/>
            <xs:element name="float4x3" type="cg_float4x3"/>
            <xs:element name="float4x4" type="cg_float4x4"/>
            <xs:element name="int" type="cg_int"/>
            <xs:element name="int1" type="cg_int1"/>
            <xs:element name="int2" type="cg_int2"/>
            <xs:element name="int3" type="cg_int3"/>
            <xs:element name="int4" type="cg_int4"/>
            <xs:element name="int1x1" type="cg_int1x1"/>
            <xs:element name="int1x2" type="cg_int1x2"/>
            <xs:element name="int1x3" type="cg_int1x3"/>
            <xs:element name="int1x4" type="cg_int1x4"/>
            <xs:element name="int2x1" type="cg_int2x1"/>
            <xs:element name="int2x2" type="cg_int2x2"/>
            <xs:element name="int2x3" type="cg_int2x3"/>
            <xs:element name="int2x4" type="cg_int2x4"/>
            <xs:element name="int3x1" type="cg_int3x1"/>
            <xs:element name="int3x2" type="cg_int3x2"/>
            <xs:element name="int3x3" type="cg_int3x3"/>
            <xs:element name="int3x4" type="cg_int3x4"/>
            <xs:element name="int4x1" type="cg_int4x1"/>
            <xs:element name="int4x2" type="cg_int4x2"/>
            <xs:element name="int4x3" type="cg_int4x3"/>
            <xs:element name="int4x4" type="cg_int4x4"/>
            <xs:element name="half" type="cg_half"/>
            <xs:element name="half1" type="cg_half1"/>
            <xs:element name="half2" type="cg_half2"/>
            <xs:element name="half3" type="cg_half3"/>
            <xs:element name="half4" type="cg_half4"/>
            <xs:element name="half1x1" type="cg_half1x1"/>
            <xs:element name="half1x2" type="cg_half1x2"/>
            <xs:element name="half1x3" type="cg_half1x3"/>
            <xs:element name="half1x4" type="cg_half1x4"/>
            <xs:element name="half2x1" type="cg_half2x1"/>
            <xs:element name="half2x2" type="cg_half2x2"/>
            <xs:element name="half2x3" type="cg_half2x3"/>
            <xs:element name="half2x4" type="cg_half2x4"/>
            <xs:element name="half3x1" type="cg_half3x1"/>
            <xs:element name="half3x2" type="cg_half3x2"/>
            <xs:element name="half3x3" type="cg_half3x3"/>
            <xs:element name="half3x4" type="cg_half3x4"/>
            <xs:element name="half4x1" type="cg_half4x1"/>
            <xs:element name="half4x2" type="cg_half4x2"/>
            <xs:element name="half4x3" type="cg_half4x3"/>
            <xs:element name="half4x4" type="cg_half4x4"/>
            <xs:element name="fixed" type="cg_fixed"/>
            <xs:element name="fixed1" type="cg_fixed1"/>
            <xs:element name="fixed2" type="cg_fixed2"/>
            <xs:element name="fixed3" type="cg_fixed3"/>
            <xs:element name="fixed4" type="cg_fixed4"/>
            <xs:element name="fixed1x1" type="cg_fixed1x1"/>
            <xs:element name="fixed1x2" type="cg_fixed1x2"/>
            <xs:element name="fixed1x3" type="cg_fixed1x3"/>
            <xs:element name="fixed1x4" type="cg_fixed1x4"/>
            <xs:element name="fixed2x1" type="cg_fixed2x1"/>
            <xs:element name="fixed2x2" type="cg_fixed2x2"/>
            <xs:element name="fixed2x3" type="cg_fixed2x3"/>
            <xs:element name="fixed2x4" type="cg_fixed2x4"/>
            <xs:element name="fixed3x1" type="cg_fixed3x1"/>
            <xs:element name="fixed3x2" type="cg_fixed3x2"/>
            <xs:element name="fixed3x3" type="cg_fixed3x3"/>
            <xs:element name="fixed3x4" type="cg_fixed3x4"/>
            <xs:element name="fixed4x1" type="cg_fixed4x1"/>
            <xs:element name="fixed4x2" type="cg_fixed4x2"/>
            <xs:element name="fixed4x3" type="cg_fixed4x3"/>
            <xs:element name="fixed4x4" type="cg_fixed4x4"/>
            <xs:element name="surface" type="cg_surface_type"/>
            <xs:element name="sampler1D" type="cg_sampler1D"/>
            <xs:element name="sampler2D" type="cg_sampler2D"/>
            <xs:element name="sampler3D" type="cg_sampler3D"/>
            <xs:element name="samplerRECT" type="cg_samplerRECT"/>
            <xs:element name="samplerCUBE" type="cg_samplerCUBE"/>
            <xs:element name="samplerDEPTH" type="cg_samplerDEPTH"/>
            <xs:element name="string" type="xs:string"/>
            <xs:element name="enum" type="gl_enumeration"/>
        </xs:choice>
    </xs:group>
    <xs:complexType name="cg_newparam">
        <xs:annotation>
            <xs:documentation>
            Create a new, named param object in the CG Runtime, assign it a type, an initial value, and additional attributes at declaration time.
            </xs:documentation>
        </xs:annotation>
        <xs:sequence>
            <xs:element name="annotate" type="fx_annotate_common" minOccurs="0" maxOccurs="unbounded">
                <xs:annotation>
                    <xs:documentation>
                    The annotate element allows you to specify an annotation for this new param.
                    </xs:documentation>
                </xs:annotation>
            </xs:element>
            <xs:element name="semantic" type="xs:NCName" minOccurs="0">
                <xs:annotation>
                    <xs:documentation>
                    The semantic element allows you to specify a semantic for this new param.
                    </xs:documentation>
                </xs:annotation>
            </xs:element>
            <xs:element name="modifier" type="fx_modifier_enum_common" minOccurs="0">
                <xs:annotation>
                    <xs:documentation>
                    The modifier element allows you to specify a modifier for this new param.
                    </xs:documentation>
                </xs:annotation>
            </xs:element>
            <xs:choice>
                <xs:group ref="cg_param_type"/>
                <xs:element name="usertype" type="cg_setuser_type"/>
                <xs:element name="array" type="cg_newarray_type"/>
            </xs:choice>
        </xs:sequence>
        <xs:attribute name="sid" type="cg_identifier" use="required"/>
    </xs:complexType>
    <xs:complexType name="cg_setparam_simple">
        <xs:sequence>
            <xs:element name="annotate" type="fx_annotate_common" minOccurs="0" maxOccurs="unbounded"/>
            <xs:group ref="cg_param_type"/>
        </xs:sequence>
        <xs:attribute name="ref" type="cg_identifier" use="required"/>
    </xs:complexType>
    <xs:complexType name="cg_setparam">
        <xs:annotation>
            <xs:documentation>
            Assigns a new value to a previously defined parameter.
            </xs:documentation>
        </xs:annotation>
        <xs:choice>
            <xs:group ref="cg_param_type"/>
            <xs:element name="usertype" type="cg_setuser_type"/>
            <xs:element name="array" type="cg_setarray_type"/>
            <xs:element name="connect_param" type="cg_connect_param"/>
        </xs:choice>
        <xs:attribute name="ref" type="cg_identifier" use="required"/>
        <xs:attribute name="program" type="xs:NCName"/>
    </xs:complexType>
    <xs:element name="profile_CG" substitutionGroup="fx_profile_abstract">
        <xs:annotation>
            <xs:documentation>
            Opens a block of CG platform-specific data types and technique declarations.
            </xs:documentation>
        </xs:annotation>
        <xs:complexType>
            <xs:sequence>
                <xs:element ref="asset" minOccurs="0"/>
                <xs:choice minOccurs="0" maxOccurs="unbounded">
                    <xs:element name="code" type="fx_code_profile"/>
                    <xs:element name="include" type="fx_include_common"/>
                </xs:choice>
                <xs:choice minOccurs="0" maxOccurs="unbounded">
                    <xs:element ref="image"/>
                    <xs:element name="newparam" type="cg_newparam"/>
                </xs:choice>
                <xs:element name="technique" maxOccurs="unbounded">
                    <xs:annotation>
                        <xs:documentation>
                        Holds a description of the textures, samplers, shaders, parameters, and passes necessary for rendering this effect using one method.
                        </xs:documentation>
                    </xs:annotation>
                    <xs:complexType>
                        <xs:sequence>
                            <xs:element ref="asset" minOccurs="0">
                                <xs:annotation>
                                    <xs:documentation>
                                    The technique element may contain an asset element.
                                    </xs:documentation>
                                </xs:annotation>
                            </xs:element>
                            <xs:element name="annotate" type="fx_annotate_common" minOccurs="0" maxOccurs="unbounded"/>
                            <xs:choice minOccurs="0" maxOccurs="unbounded">
                                <xs:element name="code" type="fx_code_profile"/>
                                <xs:element name="include" type="fx_include_common"/>
                            </xs:choice>
                            <xs:choice minOccurs="0" maxOccurs="unbounded">
                                <xs:element ref="image"/>
                                <xs:element name="newparam" type="cg_newparam"/>
                                <xs:element name="setparam" type="cg_setparam"/>
                            </xs:choice>
                            <xs:element name="pass" maxOccurs="unbounded">
                                <xs:annotation>
                                    <xs:documentation>
                                    A static declaration of all the render states, shaders, and settings for one rendering pipeline.
                                    </xs:documentation>
                                </xs:annotation>
                                <xs:complexType>
                                    <xs:sequence>
                                        <xs:element name="annotate" type="fx_annotate_common" minOccurs="0" maxOccurs="unbounded"/>
                                        <xs:element name="color_target" type="fx_colortarget_common" minOccurs="0" maxOccurs="unbounded"/>
                                        <xs:element name="depth_target" type="fx_depthtarget_common" minOccurs="0" maxOccurs="unbounded"/>
                                        <xs:element name="stencil_target" type="fx_stenciltarget_common" minOccurs="0" maxOccurs="unbounded"/>
                                        <xs:element name="color_clear" type="fx_clearcolor_common" minOccurs="0" maxOccurs="unbounded"/>
                                        <xs:element name="depth_clear" type="fx_cleardepth_common" minOccurs="0" maxOccurs="unbounded"/>
                                        <xs:element name="stencil_clear" type="fx_clearstencil_common" minOccurs="0" maxOccurs="unbounded"/>
                                        <xs:element name="draw" type="fx_draw_common" minOccurs="0"/>
                                        <xs:choice maxOccurs="unbounded">
                                            <xs:group ref="gl_pipeline_settings"/>
                                            <xs:element name="shader">
                                                <xs:annotation>
                                                    <xs:documentation>
                                                    Declare and prepare a shader for execution in the rendering pipeline of a pass.
                                                    </xs:documentation>
                                                </xs:annotation>
                                                <xs:complexType>
                                                    <xs:sequence>
                                                        <xs:element name="annotate" type="fx_annotate_common" minOccurs="0" maxOccurs="unbounded"/>
                                                        <xs:sequence minOccurs="0">
                                                            <xs:element name="compiler_target">
                                                                <xs:complexType>
                                                                    <xs:simpleContent>
                                                                        <xs:extension base="xs:NMTOKEN"/>
                                                                    </xs:simpleContent>
                                                                </xs:complexType>
                                                            </xs:element>
                                                            <xs:element name="compiler_options" type="xs:string" minOccurs="0">
                                                                <xs:annotation>
                                                                    <xs:documentation>
                                                                    A string containing command-line operations for the shader compiler.
                                                                    </xs:documentation>
                                                                </xs:annotation>
                                                            </xs:element>
                                                        </xs:sequence>
                                                        <xs:element name="name">
                                                            <xs:annotation>
                                                                <xs:documentation>
                                                                The entry symbol for the shader function.
                                                                </xs:documentation>
                                                            </xs:annotation>
                                                            <xs:complexType>
                                                                <xs:simpleContent>
                                                                    <xs:extension base="xs:NCName">
                                                                        <xs:attribute name="source" type="xs:NCName" use="optional"/>
                                                                    </xs:extension>
                                                                </xs:simpleContent>
                                                            </xs:complexType>
                                                        </xs:element>
                                                        <xs:element name="bind" minOccurs="0" maxOccurs="unbounded">
                                                            <xs:annotation>
                                                                <xs:documentation>
                                                                Binds values to uniform inputs of a shader.
                                                                </xs:documentation>
                                                            </xs:annotation>
                                                            <xs:complexType>
                                                                <xs:choice>
                                                                    <xs:group ref="cg_param_type"/>
                                                                    <xs:element name="param">
                                                                        <xs:annotation>
                                                                            <xs:documentation>
                                                                            References a predefined parameter in shader binding declarations.
                                                                            </xs:documentation>
                                                                        </xs:annotation>
                                                                        <xs:complexType>
                                                                            <xs:attribute name="ref" type="xs:NCName" use="required"/>
                                                                        </xs:complexType>
                                                                    </xs:element>
                                                                </xs:choice>
                                                                <xs:attribute name="symbol" type="xs:NCName" use="required">
                                                                    <xs:annotation>
                                                                        <xs:documentation>
                                                                        The identifier for a uniform input parameter to the shader (a formal function parameter or in-scope
                                                                        global) that will be bound to an external resource.
                                                                        </xs:documentation>
                                                                    </xs:annotation>
                                                                </xs:attribute>
                                                            </xs:complexType>
                                                        </xs:element>
                                                    </xs:sequence>
                                                    <xs:attribute name="stage" type="cg_pipeline_stage">
                                                        <xs:annotation>
                                                            <xs:documentation>
                                                            In which pipeline stage this programmable shader is designed to execute, for example, VERTEX, FRAGMENT, etc.
                                                            </xs:documentation>
                                                        </xs:annotation>
                                                    </xs:attribute>
                                                </xs:complexType>
                                            </xs:element>
                                        </xs:choice>
                                        <xs:element ref="extra" minOccurs="0" maxOccurs="unbounded"/>
                                    </xs:sequence>
                                    <xs:attribute name="sid" type="xs:NCName" use="optional">
                                        <xs:annotation>
                                            <xs:documentation>
                                            The sid attribute is a text string value containing the sub-identifier of this element.
                                            This value must be unique within the scope of the parent element. Optional attribute.
                                            </xs:documentation>
                                        </xs:annotation>
                                    </xs:attribute>
                                </xs:complexType>
                            </xs:element>
                            <xs:element ref="extra" minOccurs="0" maxOccurs="unbounded"/>
                        </xs:sequence>
                        <xs:attribute name="id" type="xs:ID">
                            <xs:annotation>
                                <xs:documentation>
                                The id attribute is a text string containing the unique identifier of this element.
                                This value must be unique within the instance document. Optional attribute.
                                </xs:documentation>
                            </xs:annotation>
                        </xs:attribute>
                        <xs:attribute name="sid" type="xs:NCName" use="required">
                            <xs:annotation>
                                <xs:documentation>
                                The sid attribute is a text string value containing the sub-identifier of this element.
                                This value must be unique within the scope of the parent element. Optional attribute.
                                </xs:documentation>
                            </xs:annotation>
                        </xs:attribute>
                    </xs:complexType>
                </xs:element>
                <xs:element ref="extra" minOccurs="0" maxOccurs="unbounded"/>
            </xs:sequence>
            <xs:attribute name="id" type="xs:ID" use="optional">
                <xs:annotation>
                    <xs:documentation>
                    The id attribute is a text string containing the unique identifier of this element.
                    This value must be unique within the instance document. Optional attribute.
                    </xs:documentation>
                </xs:annotation>
            </xs:attribute>
            <xs:attribute name="platform" type="xs:NCName" use="optional" default="PC">
                <xs:annotation>
                    <xs:documentation>
                    The type of platform. This is a vendor-defined character string that indicates the platform or capability target for the technique. Optional
                    </xs:documentation>
                </xs:annotation>
            </xs:attribute>
        </xs:complexType>
    </xs:element>
    <!-- =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-= -->
    <!-- COLLADA FX GLES elements                  -->
    <!-- =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-= -->
    <!-- these maximum values are from the GL.h from Khronos. Not all of them are defined in the spec -->
    <xs:simpleType name="GLES_MAX_LIGHTS_index">
        <xs:restriction base="xs:nonNegativeInteger">
            <xs:minInclusive value="0"/>
            <xs:maxExclusive value="7"/>
        </xs:restriction>
    </xs:simpleType>
    <xs:simpleType name="GLES_MAX_CLIP_PLANES_index">
        <xs:restriction base="xs:nonNegativeInteger">
            <xs:minInclusive value="0"/>
            <xs:maxExclusive value="5"/>
        </xs:restriction>
    </xs:simpleType>
    <xs:simpleType name="GLES_MAX_TEXTURE_COORDS_index">
        <xs:restriction base="xs:nonNegativeInteger">
            <xs:minInclusive value="0"/>
            <xs:maxExclusive value="8"/>
        </xs:restriction>
    </xs:simpleType>
    <xs:simpleType name="GLES_MAX_TEXTURE_IMAGE_UNITS_index">
        <xs:restriction base="xs:nonNegativeInteger">
            <xs:minInclusive value="0"/>
            <xs:maxExclusive value="31"/>
        </xs:restriction>
    </xs:simpleType>
    <xs:simpleType name="gles_texenv_mode_enums">
        <xs:restriction base="xs:token">
            <xs:enumeration value="REPLACE">
                <xs:annotation>
                    <xs:appinfo>value=0x1E01</xs:appinfo>
                </xs:annotation>
            </xs:enumeration>
            <xs:enumeration value="MODULATE">
                <xs:annotation>
                    <xs:appinfo>value=0x2100</xs:appinfo>
                </xs:annotation>
            </xs:enumeration>
            <xs:enumeration value="DECAL">
                <xs:annotation>
                    <xs:appinfo>value=0x2101</xs:appinfo>
                </xs:annotation>
            </xs:enumeration>
            <xs:enumeration value="BLEND">
                <xs:annotation>
                    <xs:appinfo>value=0x0BE2</xs:appinfo>
                </xs:annotation>
            </xs:enumeration>
            <xs:enumeration value="ADD">
                <xs:annotation>
                    <xs:appinfo>value=0x0104</xs:appinfo>
                </xs:annotation>
            </xs:enumeration>
        </xs:restriction>
    </xs:simpleType>
    <xs:complexType name="gles_texture_constant_type">
        <xs:attribute name="value" type="float4" use="optional"/>
        <xs:attribute name="param" type="xs:NCName" use="optional"/>
    </xs:complexType>
    <xs:complexType name="gles_texenv_command_type">
        <xs:sequence>
            <xs:element name="constant" type="gles_texture_constant_type" minOccurs="0"/>
        </xs:sequence>
        <xs:attribute name="operator" type="gles_texenv_mode_enums"/>
        <xs:attribute name="unit" type="xs:NCName"/>
    </xs:complexType>
    <xs:simpleType name="gles_texcombiner_operatorRGB_enums">
        <xs:restriction base="xs:token">
            <xs:enumeration value="REPLACE">
                <xs:annotation>
                    <xs:appinfo>value=0x1E01</xs:appinfo>
                </xs:annotation>
            </xs:enumeration>
            <xs:enumeration value="MODULATE">
                <xs:annotation>
                    <xs:appinfo>value=0x2100</xs:appinfo>
                </xs:annotation>
            </xs:enumeration>
            <xs:enumeration value="ADD">
                <xs:annotation>
                    <xs:appinfo>value=0x0104</xs:appinfo>
                </xs:annotation>
            </xs:enumeration>
            <xs:enumeration value="ADD_SIGNED">
                <xs:annotation>
                    <xs:appinfo>value=0x8574</xs:appinfo>
                </xs:annotation>
            </xs:enumeration>
            <xs:enumeration value="INTERPOLATE">
                <xs:annotation>
                    <xs:appinfo>value=0x8575</xs:appinfo>
                </xs:annotation>
            </xs:enumeration>
            <xs:enumeration value="SUBTRACT">
                <xs:annotation>
                    <xs:appinfo>value=0x84E7</xs:appinfo>
                </xs:annotation>
            </xs:enumeration>
            <xs:enumeration value="DOT3_RGB">
                <xs:annotation>
                    <xs:appinfo>value=0x86AE</xs:appinfo>
                </xs:annotation>
            </xs:enumeration>
            <xs:enumeration value="DOT3_RGBA">
                <xs:annotation>
                    <xs:appinfo>value=0x86AF</xs:appinfo>
                </xs:annotation>
            </xs:enumeration>
        </xs:restriction>
    </xs:simpleType>
    <xs:simpleType name="gles_texcombiner_operatorAlpha_enums">
        <xs:restriction base="xs:token">
            <xs:enumeration value="REPLACE">
                <xs:annotation>
                    <xs:appinfo>value=0x1E01</xs:appinfo>
                </xs:annotation>
            </xs:enumeration>
            <xs:enumeration value="MODULATE">
                <xs:annotation>
                    <xs:appinfo>value=0x2100</xs:appinfo>
                </xs:annotation>
            </xs:enumeration>
            <xs:enumeration value="ADD">
                <xs:annotation>
                    <xs:appinfo>value=0x0104</xs:appinfo>
                </xs:annotation>
            </xs:enumeration>
            <xs:enumeration value="ADD_SIGNED">
                <xs:annotation>
                    <xs:appinfo>value=0x8574</xs:appinfo>
                </xs:annotation>
            </xs:enumeration>
            <xs:enumeration value="INTERPOLATE">
                <xs:annotation>
                    <xs:appinfo>value=0x8575</xs:appinfo>
                </xs:annotation>
            </xs:enumeration>
            <xs:enumeration value="SUBTRACT">
                <xs:annotation>
                    <xs:appinfo>value=0x84E7</xs:appinfo>
                </xs:annotation>
            </xs:enumeration>
        </xs:restriction>
    </xs:simpleType>
    <xs:simpleType name="gles_texcombiner_source_enums">
        <xs:restriction base="xs:token">
            <xs:enumeration value="TEXTURE">
                <xs:annotation>
                    <xs:appinfo>value=0x1702</xs:appinfo>
                </xs:annotation>
            </xs:enumeration>
            <xs:enumeration value="CONSTANT">
                <xs:annotation>
                    <xs:appinfo>value=0x8576</xs:appinfo>
                </xs:annotation>
            </xs:enumeration>
            <xs:enumeration value="PRIMARY">
                <xs:annotation>
                    <xs:appinfo>value=0x8577</xs:appinfo>
                </xs:annotation>
            </xs:enumeration>
            <xs:enumeration value="PREVIOUS">
                <xs:annotation>
                    <xs:appinfo>value=0x8578</xs:appinfo>
                </xs:annotation>
            </xs:enumeration>
        </xs:restriction>
    </xs:simpleType>
    <xs:simpleType name="gles_texcombiner_operandRGB_enums">
        <xs:restriction base="gl_blend_type">
            <xs:enumeration value="SRC_COLOR">
                <xs:annotation>
                    <xs:appinfo>value=0x0300</xs:appinfo>
                </xs:annotation>
            </xs:enumeration>
            <xs:enumeration value="ONE_MINUS_SRC_COLOR">
                <xs:annotation>
                    <xs:appinfo>value=0x0301</xs:appinfo>
                </xs:annotation>
            </xs:enumeration>
            <xs:enumeration value="SRC_ALPHA">
                <xs:annotation>
                    <xs:appinfo>value=0x0302</xs:appinfo>
                </xs:annotation>
            </xs:enumeration>
            <xs:enumeration value="ONE_MINUS_SRC_ALPHA">
                <xs:annotation>
                    <xs:appinfo>value=0x0303</xs:appinfo>
                </xs:annotation>
            </xs:enumeration>
        </xs:restriction>
    </xs:simpleType>
    <xs:simpleType name="gles_texcombiner_operandAlpha_enums">
        <xs:restriction base="gl_blend_type">
            <xs:enumeration value="SRC_ALPHA">
                <xs:annotation>
                    <xs:appinfo>value=0x0302</xs:appinfo>
                </xs:annotation>
            </xs:enumeration>
            <xs:enumeration value="ONE_MINUS_SRC_ALPHA">
                <xs:annotation>
                    <xs:appinfo>value=0x0303</xs:appinfo>
                </xs:annotation>
            </xs:enumeration>
        </xs:restriction>
    </xs:simpleType>
    <xs:simpleType name="gles_texcombiner_argument_index_type">
        <xs:restriction base="xs:nonNegativeInteger">
            <xs:minInclusive value="0"/>
            <xs:maxInclusive value="2"/>
        </xs:restriction>
    </xs:simpleType>
    <xs:complexType name="gles_texcombiner_argumentRGB_type">
        <xs:attribute name="source" type="gles_texcombiner_source_enums"/>
        <xs:attribute name="operand" type="gles_texcombiner_operandRGB_enums" default="SRC_COLOR"/>
        <xs:attribute name="unit" type="xs:NCName" use="optional"/>
    </xs:complexType>
    <xs:complexType name="gles_texcombiner_argumentAlpha_type">
        <xs:attribute name="source" type="gles_texcombiner_source_enums"/>
        <xs:attribute name="operand" type="gles_texcombiner_operandAlpha_enums" default="SRC_ALPHA"/>
        <xs:attribute name="unit" type="xs:NCName" use="optional"/>
    </xs:complexType>
    <xs:complexType name="gles_texcombiner_commandRGB_type">
        <xs:annotation>
            <xs:documentation>
            Defines the RGB portion of a texture_pipeline command. This is a combiner-mode texturing operation.
            </xs:documentation>
        </xs:annotation>
        <xs:sequence>
            <xs:element name="argument" type="gles_texcombiner_argumentRGB_type" maxOccurs="3"/>
        </xs:sequence>
        <xs:attribute name="operator" type="gles_texcombiner_operatorRGB_enums"/>
        <xs:attribute name="scale" type="xs:float" use="optional"/>
    </xs:complexType>
    <xs:complexType name="gles_texcombiner_commandAlpha_type">
        <xs:sequence>
            <xs:element name="argument" type="gles_texcombiner_argumentAlpha_type" maxOccurs="3"/>
        </xs:sequence>
        <xs:attribute name="operator" type="gles_texcombiner_operatorAlpha_enums"/>
        <xs:attribute name="scale" type="xs:float" use="optional"/>
    </xs:complexType>
    <xs:complexType name="gles_texcombiner_command_type">
        <xs:sequence>
            <xs:element name="constant" type="gles_texture_constant_type" minOccurs="0"/>
            <xs:element name="RGB" type="gles_texcombiner_commandRGB_type" minOccurs="0"/>
            <xs:element name="alpha" type="gles_texcombiner_commandAlpha_type" minOccurs="0"/>
        </xs:sequence>
    </xs:complexType>
    <xs:complexType name="gles_texture_pipeline">
        <xs:annotation>
            <xs:documentation>
            Defines a set of texturing commands that will be converted into multitexturing operations using glTexEnv in regular and combiner mode.
            </xs:documentation>
        </xs:annotation>
        <xs:choice maxOccurs="unbounded">
            <xs:element name="texcombiner" type="gles_texcombiner_command_type">
                <xs:annotation>
                    <xs:documentation>
                    Defines a texture_pipeline command. This is a combiner-mode texturing operation.
                    </xs:documentation>
                </xs:annotation>
            </xs:element>
            <xs:element name="texenv" type="gles_texenv_command_type">
                <xs:annotation>
                    <xs:documentation>
                    Defines a texture_pipeline command. It is a simple noncombiner mode of texturing operations.
                    </xs:documentation>
                </xs:annotation>
            </xs:element>
            <xs:element ref="extra">
                <xs:annotation>
                    <xs:documentation>
                    The extra element may appear any number of times.
                    OpenGL ES extensions may be used here.
                    </xs:documentation>
                </xs:annotation>
            </xs:element>
        </xs:choice>
        <xs:attribute name="sid" type="xs:NCName">
            <xs:annotation>
                <xs:documentation>
                The sid attribute is a text string value containing the sub-identifier of this element.
                This value must be unique within the scope of the parent element. Optional attribute.
                </xs:documentation>
            </xs:annotation>
        </xs:attribute>
    </xs:complexType>
    <xs:complexType name="gles_texture_unit">
        <xs:sequence>
            <xs:element name="surface" type="xs:NCName" minOccurs="0"/>
            <xs:element name="sampler_state" type="xs:NCName" minOccurs="0"/>
            <xs:element name="texcoord" minOccurs="0">
                <xs:complexType>
                    <xs:attribute name="semantic" type="xs:NCName"/>
                </xs:complexType>
            </xs:element>
            <xs:element ref="extra" minOccurs="0" maxOccurs="unbounded"/>
        </xs:sequence>
        <xs:attribute name="sid" type="xs:NCName">
            <xs:annotation>
                <xs:documentation>
                The sid attribute is a text string value containing the sub-identifier of this element.
                This value must be unique within the scope of the parent element. Optional attribute.
                </xs:documentation>
            </xs:annotation>
        </xs:attribute>
    </xs:complexType>
    <xs:simpleType name="gles_sampler_wrap">
        <xs:restriction base="xs:NMTOKEN">
            <xs:enumeration value="REPEAT"/>
            <xs:enumeration value="CLAMP"/>
            <xs:enumeration value="CLAMP_TO_EDGE"/>
            <xs:enumeration value="MIRRORED_REPEAT">
                <xs:annotation>
                    <xs:documentation>
                    supported by GLES 1.1 only
                    </xs:documentation>
                </xs:annotation>
            </xs:enumeration>
        </xs:restriction>
    </xs:simpleType>
    <xs:complexType name="gles_sampler_state">
        <xs:annotation>
            <xs:documentation>
            Two-dimensional texture sampler state for profile_GLES. This is a bundle of sampler-specific states that will be referenced by one or more texture_units.
            </xs:documentation>
        </xs:annotation>
        <xs:sequence>
            <xs:element name="wrap_s" type="gles_sampler_wrap" default="REPEAT" minOccurs="0"/>
            <xs:element name="wrap_t" type="gles_sampler_wrap" default="REPEAT" minOccurs="0"/>
            <xs:element name="minfilter" type="fx_sampler_filter_common" default="NONE" minOccurs="0"/>
            <xs:element name="magfilter" type="fx_sampler_filter_common" default="NONE" minOccurs="0"/>
            <xs:element name="mipfilter" type="fx_sampler_filter_common" default="NONE" minOccurs="0"/>
            <xs:element name="mipmap_maxlevel" type="xs:unsignedByte" default="255" minOccurs="0"/>
            <!-- perhaps bias not really supported but can be kludged in the app somewhat-->
            <xs:element name="mipmap_bias" type="xs:float" default="0.0" minOccurs="0"/>
            <xs:element ref="extra" minOccurs="0" maxOccurs="unbounded">
                <xs:annotation>
                    <xs:documentation>
                    The extra element may appear any number of times.
                    OpenGL ES extensions may be used here.
                    </xs:documentation>
                </xs:annotation>
            </xs:element>
        </xs:sequence>
        <xs:attribute name="sid" type="xs:NCName">
            <xs:annotation>
                <xs:documentation>
                The sid attribute is a text string value containing the sub-identifier of this element.
                This value must be unique within the scope of the parent element. Optional attribute.
                </xs:documentation>
            </xs:annotation>
        </xs:attribute>
    </xs:complexType>
    <xs:simpleType name="gles_stencil_op_type">
        <xs:restriction base="xs:string">
            <xs:enumeration value="KEEP">
                <xs:annotation>
                    <xs:appinfo>value=0x1E00</xs:appinfo>
                </xs:annotation>
            </xs:enumeration>
            <xs:enumeration value="ZERO">
                <xs:annotation>
                    <xs:appinfo>value=0x0</xs:appinfo>
                </xs:annotation>
            </xs:enumeration>
            <xs:enumeration value="REPLACE">
                <xs:annotation>
                    <xs:appinfo>value=0x1E01</xs:appinfo>
                </xs:annotation>
            </xs:enumeration>
            <xs:enumeration value="INCR">
                <xs:annotation>
                    <xs:appinfo>value=0x1E02</xs:appinfo>
                </xs:annotation>
            </xs:enumeration>
            <xs:enumeration value="DECR">
                <xs:annotation>
                    <xs:appinfo>value=0x1E03</xs:appinfo>
                </xs:annotation>
            </xs:enumeration>
            <xs:enumeration value="INVERT">
                <xs:annotation>
                    <xs:appinfo>value=0x150A</xs:appinfo>
                </xs:annotation>
            </xs:enumeration>
        </xs:restriction>
    </xs:simpleType>
    <xs:simpleType name="gles_enumeration">
        <xs:union memberTypes="gl_blend_type gl_face_type gl_func_type gl_stencil_op_type gl_material_type gl_fog_type gl_front_face_type gl_light_model_color_control_type gl_logic_op_type gl_polygon_mode_type gl_shade_model_type"/>
    </xs:simpleType>
    <xs:group name="gles_pipeline_settings">
        <xs:annotation>
            <xs:documentation>
            A group that contains the renderstates available for the GLES profile.
            </xs:documentation>
        </xs:annotation>
        <xs:choice>
            <xs:element name="alpha_func">
                <xs:complexType>
                    <xs:sequence>
                        <xs:element name="func">
                            <xs:complexType>
                                <xs:attribute name="value" type="gl_func_type" use="optional" default="ALWAYS"/>
                                <xs:attribute name="param" type="xs:NCName" use="optional"/>
                            </xs:complexType>
                        </xs:element>
                        <xs:element name="value">
                            <xs:complexType>
                                <xs:attribute name="value" type="gl_alpha_value_type" use="optional" default="0.0"/>
                                <xs:attribute name="param" type="xs:NCName" use="optional"/>
                            </xs:complexType>
                        </xs:element>
                    </xs:sequence>
                </xs:complexType>
            </xs:element>
            <xs:element name="blend_func">
                <xs:complexType>
                    <xs:sequence>
                        <xs:element name="src">
                            <xs:complexType>
                                <xs:attribute name="value" type="gl_blend_type" use="optional" default="ONE"/>
                                <xs:attribute name="param" type="xs:NCName" use="optional"/>
                            </xs:complexType>
                        </xs:element>
                        <xs:element name="dest">
                            <xs:complexType>
                                <xs:attribute name="value" type="gl_blend_type" use="optional" default="ZERO"/>
                                <xs:attribute name="param" type="xs:NCName" use="optional"/>
                            </xs:complexType>
                        </xs:element>
                    </xs:sequence>
                </xs:complexType>
            </xs:element>
            <xs:element name="clear_color">
                <xs:complexType>
                    <xs:attribute name="value" type="float4" use="optional"/>
                    <xs:attribute name="param" type="xs:NCName" use="optional"/>
                </xs:complexType>
            </xs:element>
            <xs:element name="clear_stencil">
                <xs:complexType>
                    <xs:attribute name="value" type="int" use="optional"/>
                    <xs:attribute name="param" type="xs:NCName" use="optional"/>
                </xs:complexType>
            </xs:element>
            <xs:element name="clear_depth">
                <xs:complexType>
                    <xs:attribute name="value" type="float" use="optional"/>
                    <xs:attribute name="param" type="xs:NCName" use="optional"/>
                </xs:complexType>
            </xs:element>
            <xs:element name="clip_plane">
                <xs:complexType>
                    <xs:attribute name="value" type="bool4" use="optional"/>
                    <xs:attribute name="param" type="xs:NCName" use="optional"/>
                    <xs:attribute name="index" type="GLES_MAX_CLIP_PLANES_index" use="required"/>
                </xs:complexType>
            </xs:element>
            <xs:element name="color_mask">
                <xs:complexType>
                    <xs:attribute name="value" type="bool4" use="optional"/>
                    <xs:attribute name="param" type="xs:NCName" use="optional"/>
                </xs:complexType>
            </xs:element>
            <xs:element name="cull_face">
                <xs:complexType>
                    <xs:attribute name="value" type="gl_face_type" use="optional" default="BACK"/>
                    <xs:attribute name="param" type="xs:NCName" use="optional"/>
                </xs:complexType>
            </xs:element>
            <xs:element name="depth_func">
                <xs:complexType>
                    <xs:attribute name="value" type="gl_func_type" use="optional" default="ALWAYS"/>
                    <xs:attribute name="param" type="xs:NCName" use="optional"/>
                </xs:complexType>
            </xs:element>
            <xs:element name="depth_mask">
                <xs:complexType>
                    <xs:attribute name="value" type="bool" use="optional" default="false"/>
                    <xs:attribute name="param" type="xs:NCName" use="optional"/>
                </xs:complexType>
            </xs:element>
            <xs:element name="depth_range">
                <xs:complexType>
                    <xs:attribute name="value" type="float2" use="optional" default="0 1"/>
                    <xs:attribute name="param" type="xs:NCName" use="optional"/>
                </xs:complexType>
            </xs:element>
            <xs:element name="fog_color">
                <xs:complexType>
                    <xs:attribute name="value" type="float4" use="optional" default="0 0 0 0"/>
                    <xs:attribute name="param" type="xs:NCName" use="optional"/>
                </xs:complexType>
            </xs:element>
            <xs:element name="fog_density">
                <xs:complexType>
                    <xs:attribute name="value" type="float" use="optional" default="1"/>
                    <xs:attribute name="param" type="xs:NCName" use="optional"/>
                </xs:complexType>
            </xs:element>
            <xs:element name="fog_mode">
                <xs:complexType>
                    <xs:attribute name="value" type="gl_fog_type" use="optional" default="EXP"/>
                    <xs:attribute name="param" type="xs:NCName" use="optional"/>
                </xs:complexType>
            </xs:element>
            <xs:element name="fog_start">
                <xs:complexType>
                    <xs:attribute name="value" type="float" use="optional" default="0"/>
                    <xs:attribute name="param" type="xs:NCName" use="optional"/>
                </xs:complexType>
            </xs:element>
            <xs:element name="fog_end">
                <xs:complexType>
                    <xs:attribute name="value" type="float" use="optional" default="1"/>
                    <xs:attribute name="param" type="xs:NCName" use="optional"/>
                </xs:complexType>
            </xs:element>
            <xs:element name="front_face">
                <xs:complexType>
                    <xs:attribute name="value" type="gl_front_face_type" use="optional" default="CCW"/>
                    <xs:attribute name="param" type="xs:NCName" use="optional"/>
                </xs:complexType>
            </xs:element>
            <xs:element name="texture_pipeline">
                <xs:complexType>
                    <xs:sequence>
                        <xs:element name="value" type="gles_texture_pipeline" minOccurs="0"/>
                    </xs:sequence>
                    <xs:attribute name="param" type="xs:NCName" use="optional"/>
                </xs:complexType>
            </xs:element>
            <xs:element name="logic_op">
                <xs:complexType>
                    <xs:attribute name="value" type="gl_logic_op_type" use="optional" default="COPY"/>
                    <xs:attribute name="param" type="xs:NCName" use="optional"/>
                </xs:complexType>
            </xs:element>
            <xs:element name="light_ambient">
                <xs:complexType>
                    <xs:attribute name="value" type="float4" use="optional" default="0 0 0 1"/>
                    <xs:attribute name="param" type="xs:NCName" use="optional"/>
                    <xs:attribute name="index" type="GLES_MAX_LIGHTS_index" use="required"/>
                </xs:complexType>
            </xs:element>
            <xs:element name="light_diffuse">
                <xs:complexType>
                    <xs:attribute name="value" type="float4" use="optional" default="0 0 0 0"/>
                    <xs:attribute name="param" type="xs:NCName" use="optional"/>
                    <xs:attribute name="index" type="GLES_MAX_LIGHTS_index" use="required"/>
                </xs:complexType>
            </xs:element>
            <xs:element name="light_specular">
                <xs:complexType>
                    <xs:attribute name="value" type="float4" use="optional" default="0 0 0 0"/>
                    <xs:attribute name="param" type="xs:NCName" use="optional"/>
                    <xs:attribute name="index" type="GLES_MAX_LIGHTS_index" use="required"/>
                </xs:complexType>
            </xs:element>
            <xs:element name="light_position">
                <xs:complexType>
                    <xs:attribute name="value" type="float4" use="optional" default="0 0 1 0"/>
                    <xs:attribute name="param" type="xs:NCName" use="optional"/>
                    <xs:attribute name="index" type="GLES_MAX_LIGHTS_index" use="required"/>
                </xs:complexType>
            </xs:element>
            <xs:element name="light_constant_attenuation">
                <xs:complexType>
                    <xs:attribute name="value" type="float" use="optional" default="1"/>
                    <xs:attribute name="param" type="xs:NCName" use="optional"/>
                    <xs:attribute name="index" type="GLES_MAX_LIGHTS_index" use="required"/>
                </xs:complexType>
            </xs:element>
            <xs:element name="light_linear_attenutation">
                <xs:complexType>
                    <xs:attribute name="value" type="float" use="optional" default="1"/>
                    <xs:attribute name="param" type="xs:NCName" use="optional"/>
                    <xs:attribute name="index" type="GLES_MAX_LIGHTS_index" use="required"/>
                </xs:complexType>
            </xs:element>
            <xs:element name="light_quadratic_attenuation">
                <xs:complexType>
                    <xs:attribute name="value" type="float" use="optional" default="1"/>
                    <xs:attribute name="param" type="xs:NCName" use="optional"/>
                    <xs:attribute name="index" type="GLES_MAX_LIGHTS_index" use="required"/>
                </xs:complexType>
            </xs:element>
            <xs:element name="light_spot_cutoff">
                <xs:complexType>
                    <xs:attribute name="value" type="float" use="optional" default="180"/>
                    <xs:attribute name="param" type="xs:NCName" use="optional"/>
                    <xs:attribute name="index" type="GLES_MAX_LIGHTS_index" use="required"/>
                </xs:complexType>
            </xs:element>
            <xs:element name="light_spot_direction">
                <xs:complexType>
                    <xs:attribute name="value" type="float3" use="optional" default="0 0 -1"/>
                    <xs:attribute name="param" type="xs:NCName" use="optional"/>
                    <xs:attribute name="index" type="GLES_MAX_LIGHTS_index" use="required"/>
                </xs:complexType>
            </xs:element>
            <xs:element name="light_spot_exponent">
                <xs:complexType>
                    <xs:attribute name="value" type="float" use="optional" default="0"/>
                    <xs:attribute name="param" type="xs:NCName" use="optional"/>
                    <xs:attribute name="index" type="GLES_MAX_LIGHTS_index" use="required"/>
                </xs:complexType>
            </xs:element>
            <xs:element name="light_model_ambient">
                <xs:complexType>
                    <xs:attribute name="value" type="float4" use="optional" default="0.2 0.2 0.2 1.0"/>
                    <xs:attribute name="param" type="xs:NCName" use="optional"/>
                </xs:complexType>
            </xs:element>
            <xs:element name="line_width">
                <xs:complexType>
                    <xs:attribute name="value" type="float" use="optional" default="1"/>
                    <xs:attribute name="param" type="xs:NCName" use="optional"/>
                </xs:complexType>
            </xs:element>
            <xs:element name="material_ambient">
                <xs:complexType>
                    <xs:attribute name="value" type="float4" use="optional" default="0.2 0.2 0.2 1.0"/>
                    <xs:attribute name="param" type="xs:NCName" use="optional"/>
                </xs:complexType>
            </xs:element>
            <xs:element name="material_diffuse">
                <xs:complexType>
                    <xs:attribute name="value" type="float4" use="optional" default="0.8 0.8 0.8 1.0"/>
                    <xs:attribute name="param" type="xs:NCName" use="optional"/>
                </xs:complexType>
            </xs:element>
            <xs:element name="material_emission">
                <xs:complexType>
                    <xs:attribute name="value" type="float4" use="optional" default="0 0 0 1"/>
                    <xs:attribute name="param" type="xs:NCName" use="optional"/>
                </xs:complexType>
            </xs:element>
            <xs:element name="material_shininess">
                <xs:complexType>
                    <xs:attribute name="value" type="float" use="optional" default="0"/>
                    <xs:attribute name="param" type="xs:NCName" use="optional"/>
                </xs:complexType>
            </xs:element>
            <xs:element name="material_specular">
                <xs:complexType>
                    <xs:attribute name="value" type="float4" use="optional" default="0 0 0 1"/>
                    <xs:attribute name="param" type="xs:NCName" use="optional"/>
                </xs:complexType>
            </xs:element>
            <xs:element name="model_view_matrix">
                <xs:complexType>
                    <xs:attribute name="value" type="float4x4" use="optional" default="1 0 0 0 0 1 0 0 0 0 1 0 0 0 0 1"/>
                    <xs:attribute name="param" type="xs:NCName" use="optional"/>
                </xs:complexType>
            </xs:element>
            <xs:element name="point_distance_attenuation">
                <xs:complexType>
                    <xs:attribute name="value" type="float3" use="optional" default="1 0 0"/>
                    <xs:attribute name="param" type="xs:NCName" use="optional"/>
                </xs:complexType>
            </xs:element>
            <xs:element name="point_fade_threshold_size">
                <xs:complexType>
                    <xs:attribute name="value" type="float" use="optional" default="1"/>
                    <xs:attribute name="param" type="xs:NCName" use="optional"/>
                </xs:complexType>
            </xs:element>
            <xs:element name="point_size">
                <xs:complexType>
                    <xs:attribute name="value" type="float" use="optional" default="1"/>
                    <xs:attribute name="param" type="xs:NCName" use="optional"/>
                </xs:complexType>
            </xs:element>
            <xs:element name="point_size_min">
                <xs:complexType>
                    <xs:attribute name="value" type="float" use="optional" default="0"/>
                    <xs:attribute name="param" type="xs:NCName" use="optional"/>
                </xs:complexType>
            </xs:element>
            <xs:element name="point_size_max">
                <xs:complexType>
                    <xs:attribute name="value" type="float" use="optional" default="1"/>
                    <xs:attribute name="param" type="xs:NCName" use="optional"/>
                </xs:complexType>
            </xs:element>
            <xs:element name="polygon_offset">
                <xs:complexType>
                    <xs:attribute name="value" type="float2" use="optional" default="0 0"/>
                    <xs:attribute name="param" type="xs:NCName" use="optional"/>
                </xs:complexType>
            </xs:element>
            <xs:element name="projection_matrix">
                <xs:complexType>
                    <xs:attribute name="value" type="float4x4" use="optional" default="1 0 0 0 0 1 0 0 0 0 1 0 0 0 0 1"/>
                    <xs:attribute name="param" type="xs:NCName" use="optional"/>
                </xs:complexType>
            </xs:element>
            <xs:element name="scissor">
                <xs:complexType>
                    <xs:attribute name="value" type="int4" use="optional"/>
                    <xs:attribute name="param" type="xs:NCName" use="optional"/>
                </xs:complexType>
            </xs:element>
            <xs:element name="shade_model">
                <xs:complexType>
                    <xs:attribute name="value" type="gl_shade_model_type" use="optional" default="SMOOTH"/>
                    <xs:attribute name="param" type="xs:NCName" use="optional"/>
                </xs:complexType>
            </xs:element>
            <xs:element name="stencil_func">
                <xs:complexType>
                    <xs:sequence>
                        <xs:element name="func">
                            <xs:complexType>
                                <xs:attribute name="value" type="gl_func_type" use="optional" default="ALWAYS"/>
                                <xs:attribute name="param" type="xs:NCName" use="optional"/>
                            </xs:complexType>
                        </xs:element>
                        <xs:element name="ref">
                            <xs:complexType>
                                <xs:attribute name="value" type="xs:unsignedByte" use="optional" default="0"/>
                                <xs:attribute name="param" type="xs:NCName" use="optional"/>
                            </xs:complexType>
                        </xs:element>
                        <xs:element name="mask">
                            <xs:complexType>
                                <xs:attribute name="value" type="xs:unsignedByte" use="optional" default="255"/>
                                <xs:attribute name="param" type="xs:NCName" use="optional"/>
                            </xs:complexType>
                        </xs:element>
                    </xs:sequence>
                </xs:complexType>
            </xs:element>
            <xs:element name="stencil_mask">
                <xs:complexType>
                    <xs:attribute name="value" type="int" use="optional" default="4294967295"/>
                    <xs:attribute name="param" type="xs:NCName" use="optional"/>
                </xs:complexType>
            </xs:element>
            <xs:element name="stencil_op">
                <xs:complexType>
                    <xs:sequence>
                        <xs:element name="fail">
                            <xs:complexType>
                                <xs:attribute name="value" type="gles_stencil_op_type" use="optional" default="KEEP"/>
                                <xs:attribute name="param" type="xs:NCName" use="optional"/>
                            </xs:complexType>
                        </xs:element>
                        <xs:element name="zfail">
                            <xs:complexType>
                                <xs:attribute name="value" type="gles_stencil_op_type" use="optional" default="KEEP"/>
                                <xs:attribute name="param" type="xs:NCName" use="optional"/>
                            </xs:complexType>
                        </xs:element>
                        <xs:element name="zpass">
                            <xs:complexType>
                                <xs:attribute name="value" type="gles_stencil_op_type" use="optional" default="KEEP"/>
                                <xs:attribute name="param" type="xs:NCName" use="optional"/>
                            </xs:complexType>
                        </xs:element>
                    </xs:sequence>
                </xs:complexType>
            </xs:element>
            <xs:element name="alpha_test_enable">
                <xs:complexType>
                    <xs:attribute name="value" type="bool" use="optional" default="false"/>
                    <xs:attribute name="param" type="xs:NCName" use="optional"/>
                </xs:complexType>
            </xs:element>
            <xs:element name="blend_enable">
                <xs:complexType>
                    <xs:attribute name="value" type="bool" use="optional" default="false"/>
                    <xs:attribute name="param" type="xs:NCName" use="optional"/>
                </xs:complexType>
            </xs:element>
            <xs:element name="clip_plane_enable">
                <xs:complexType>
                    <xs:attribute name="value" type="bool" use="optional" default="false"/>
                    <xs:attribute name="param" type="xs:NCName" use="optional"/>
                    <xs:attribute name="index" type="GLES_MAX_CLIP_PLANES_index"/>
                </xs:complexType>
            </xs:element>
            <xs:element name="color_logic_op_enable">
                <xs:complexType>
                    <xs:attribute name="value" type="bool" use="optional" default="false"/>
                    <xs:attribute name="param" type="xs:NCName" use="optional"/>
                </xs:complexType>
            </xs:element>
            <xs:element name="color_material_enable">
                <xs:complexType>
                    <xs:attribute name="value" type="bool" use="optional" default="true"/>
                    <xs:attribute name="param" type="xs:NCName" use="optional"/>
                </xs:complexType>
            </xs:element>
            <xs:element name="cull_face_enable">
                <xs:complexType>
                    <xs:attribute name="value" type="bool" use="optional" default="false"/>
                    <xs:attribute name="param" type="xs:NCName" use="optional"/>
                </xs:complexType>
            </xs:element>
            <xs:element name="depth_test_enable">
                <xs:complexType>
                    <xs:attribute name="value" type="bool" use="optional" default="false"/>
                    <xs:attribute name="param" type="xs:NCName" use="optional"/>
                </xs:complexType>
            </xs:element>
            <xs:element name="dither_enable">
                <xs:complexType>
                    <xs:attribute name="value" type="bool" use="optional" default="false"/>
                    <xs:attribute name="param" type="xs:NCName" use="optional"/>
                </xs:complexType>
            </xs:element>
            <xs:element name="fog_enable">
                <xs:complexType>
                    <xs:attribute name="value" type="bool" use="optional" default="false"/>
                    <xs:attribute name="param" type="xs:NCName" use="optional"/>
                </xs:complexType>
            </xs:element>
            <xs:element name="texture_pipeline_enable">
                <xs:complexType>
                    <xs:attribute name="value" type="bool" use="optional" default="false"/>
                    <xs:attribute name="param" type="xs:NCName" use="optional"/>
                </xs:complexType>
            </xs:element>
            <xs:element name="light_enable">
                <xs:complexType>
                    <xs:attribute name="value" type="bool" use="optional" default="false"/>
                    <xs:attribute name="param" type="xs:NCName" use="optional"/>
                    <xs:attribute name="index" type="GLES_MAX_LIGHTS_index" use="required"/>
                </xs:complexType>
            </xs:element>
            <xs:element name="lighting_enable">
                <xs:complexType>
                    <xs:attribute name="value" type="bool" use="optional" default="false"/>
                    <xs:attribute name="param" type="xs:NCName" use="optional"/>
                </xs:complexType>
            </xs:element>
            <xs:element name="light_model_two_side_enable">
                <xs:complexType>
                    <xs:attribute name="value" type="bool" use="optional" default="false"/>
                    <xs:attribute name="param" type="xs:NCName" use="optional"/>
                </xs:complexType>
            </xs:element>
            <xs:element name="line_smooth_enable">
                <xs:complexType>
                    <xs:attribute name="value" type="bool" use="optional" default="false"/>
                    <xs:attribute name="param" type="xs:NCName" use="optional"/>
                </xs:complexType>
            </xs:element>
            <xs:element name="multisample_enable">
                <xs:complexType>
                    <xs:attribute name="value" type="bool" use="optional" default="false"/>
                    <xs:attribute name="param" type="xs:NCName" use="optional"/>
                </xs:complexType>
            </xs:element>
            <xs:element name="normalize_enable">
                <xs:complexType>
                    <xs:attribute name="value" type="bool" use="optional" default="false"/>
                    <xs:attribute name="param" type="xs:NCName" use="optional"/>
                </xs:complexType>
            </xs:element>
            <xs:element name="point_smooth_enable">
                <xs:complexType>
                    <xs:attribute name="value" type="bool" use="optional" default="false"/>
                    <xs:attribute name="param" type="xs:NCName" use="optional"/>
                </xs:complexType>
            </xs:element>
            <xs:element name="polygon_offset_fill_enable">
                <xs:complexType>
                    <xs:attribute name="value" type="bool" use="optional" default="false"/>
                    <xs:attribute name="param" type="xs:NCName" use="optional"/>
                </xs:complexType>
            </xs:element>
            <xs:element name="rescale_normal_enable">
                <xs:complexType>
                    <xs:attribute name="value" type="bool" use="optional" default="false"/>
                    <xs:attribute name="param" type="xs:NCName" use="optional"/>
                </xs:complexType>
            </xs:element>
            <xs:element name="sample_alpha_to_coverage_enable">
                <xs:complexType>
                    <xs:attribute name="value" type="bool" use="optional" default="false"/>
                    <xs:attribute name="param" type="xs:NCName" use="optional"/>
                </xs:complexType>
            </xs:element>
            <xs:element name="sample_alpha_to_one_enable">
                <xs:complexType>
                    <xs:attribute name="value" type="bool" use="optional" default="false"/>
                    <xs:attribute name="param" type="xs:NCName" use="optional"/>
                </xs:complexType>
            </xs:element>
            <xs:element name="sample_coverage_enable">
                <xs:complexType>
                    <xs:attribute name="value" type="bool" use="optional" default="false"/>
                    <xs:attribute name="param" type="xs:NCName" use="optional"/>
                </xs:complexType>
            </xs:element>
            <xs:element name="scissor_test_enable">
                <xs:complexType>
                    <xs:attribute name="value" type="bool" use="optional" default="false"/>
                    <xs:attribute name="param" type="xs:NCName" use="optional"/>
                </xs:complexType>
            </xs:element>
            <xs:element name="stencil_test_enable">
                <xs:complexType>
                    <xs:attribute name="value" type="bool" use="optional" default="false"/>
                    <xs:attribute name="param" type="xs:NCName" use="optional"/>
                </xs:complexType>
            </xs:element>
        </xs:choice>
    </xs:group>
    <!-- - - - - - - - - - - - - - - - - - - - -->
    <xs:group name="gles_basic_type_common">
        <xs:annotation>
            <xs:documentation>
            A group that defines the available variable types for GLES parameters.
            </xs:documentation>
        </xs:annotation>
        <xs:choice>
            <xs:element name="bool" type="bool"/>
            <xs:element name="bool2" type="bool2"/>
            <xs:element name="bool3" type="bool3"/>
            <xs:element name="bool4" type="bool4"/>
            <xs:element name="int" type="int"/>
            <xs:element name="int2" type="int2"/>
            <xs:element name="int3" type="int3"/>
            <xs:element name="int4" type="int4"/>
            <xs:element name="float" type="float"/>
            <xs:element name="float2" type="float2"/>
            <xs:element name="float3" type="float3"/>
            <xs:element name="float4" type="float4"/>
            <xs:element name="float1x1" type="float"/>
            <xs:element name="float1x2" type="float2"/>
            <xs:element name="float1x3" type="float3"/>
            <xs:element name="float1x4" type="float4"/>
            <xs:element name="float2x1" type="float2"/>
            <xs:element name="float2x2" type="float2x2"/>
            <xs:element name="float2x3" type="float2x3"/>
            <xs:element name="float2x4" type="float2x4"/>
            <xs:element name="float3x1" type="float3"/>
            <xs:element name="float3x2" type="float3x2"/>
            <xs:element name="float3x3" type="float3x3"/>
            <xs:element name="float3x4" type="float3x4"/>
            <xs:element name="float4x1" type="float4"/>
            <xs:element name="float4x2" type="float4x2"/>
            <xs:element name="float4x3" type="float4x3"/>
            <xs:element name="float4x4" type="float4x4"/>
            <xs:element name="surface" type="fx_surface_common"/>
            <xs:element name="texture_pipeline" type="gles_texture_pipeline"/>
            <xs:element name="sampler_state" type="gles_sampler_state"/>
            <xs:element name="texture_unit" type="gles_texture_unit"/>
            <xs:element name="enum" type="gles_enumeration"/>
        </xs:choice>
    </xs:group>
    <xs:complexType name="gles_newparam">
        <xs:annotation>
            <xs:documentation>
            Create a new, named param object in the GLES Runtime, assign it a type, an initial value, and additional attributes at declaration time.
            </xs:documentation>
        </xs:annotation>
        <xs:sequence>
            <xs:element name="annotate" type="fx_annotate_common" minOccurs="0" maxOccurs="unbounded">
                <xs:annotation>
                    <xs:documentation>
                    The annotate element allows you to specify an annotation for this new param.
                    </xs:documentation>
                </xs:annotation>
            </xs:element>
            <xs:element name="semantic" type="xs:NCName" minOccurs="0">
                <xs:annotation>
                    <xs:documentation>
                    The semantic element allows you to specify a semantic for this new param.
                    </xs:documentation>
                </xs:annotation>
            </xs:element>
            <xs:element name="modifier" type="fx_modifier_enum_common" minOccurs="0">
                <xs:annotation>
                    <xs:documentation>
                    The modifier element allows you to specify a modifier for this new param.
                    </xs:documentation>
                </xs:annotation>
            </xs:element>
            <xs:group ref="gles_basic_type_common"/>
        </xs:sequence>
        <xs:attribute name="sid" type="xs:NCName" use="required">
            <xs:annotation>
                <xs:documentation>
                The sid attribute is a text string value containing the sub-identifier of this element.
                This value must be unique within the scope of the parent element.
                </xs:documentation>
            </xs:annotation>
        </xs:attribute>
    </xs:complexType>
    <xs:simpleType name="gles_rendertarget_common">
        <xs:restriction base="xs:NCName"/>
    </xs:simpleType>
    <xs:element name="profile_GLES" substitutionGroup="fx_profile_abstract">
        <xs:annotation>
            <xs:documentation>
            Opens a block of GLES platform-specific data types and technique declarations.
            </xs:documentation>
        </xs:annotation>
        <xs:complexType>
            <xs:sequence>
                <xs:element ref="asset" minOccurs="0"/>
                <xs:choice minOccurs="0" maxOccurs="unbounded">
                    <xs:element ref="image"/>
                    <xs:element name="newparam" type="gles_newparam"/>
                </xs:choice>
                <xs:element name="technique" maxOccurs="unbounded">
                    <xs:annotation>
                        <xs:documentation>
                        Holds a description of the textures, samplers, shaders, parameters, and passes necessary for rendering this effect using one method.
                        </xs:documentation>
                    </xs:annotation>
                    <xs:complexType>
                        <xs:sequence>
                            <xs:element ref="asset" minOccurs="0"/>
                            <xs:element name="annotate" type="fx_annotate_common" minOccurs="0" maxOccurs="unbounded"/>
                            <xs:choice minOccurs="0" maxOccurs="unbounded">
                                <xs:element ref="image"/>
                                <xs:element name="newparam" type="gles_newparam"/>
                                <xs:element name="setparam">
                                    <xs:complexType>
                                        <xs:sequence>
                                            <xs:element name="annotate" type="fx_annotate_common" minOccurs="0" maxOccurs="unbounded"/>
                                            <xs:group ref="gles_basic_type_common"/>
                                        </xs:sequence>
                                        <xs:attribute name="ref" type="xs:NCName" use="required"/>
                                    </xs:complexType>
                                </xs:element>
                            </xs:choice>
                            <xs:element name="pass" maxOccurs="unbounded">
                                <xs:annotation>
                                    <xs:documentation>
                                    A static declaration of all the render states, shaders, and settings for one rendering pipeline.
                                    </xs:documentation>
                                </xs:annotation>
                                <xs:complexType>
                                    <xs:sequence>
                                        <xs:element name="annotate" type="fx_annotate_common" minOccurs="0" maxOccurs="unbounded"/>
                                        <xs:element name="color_target" type="gles_rendertarget_common" minOccurs="0"/>
                                        <xs:element name="depth_target" type="gles_rendertarget_common" minOccurs="0"/>
                                        <xs:element name="stencil_target" type="gles_rendertarget_common" minOccurs="0"/>
                                        <xs:element name="color_clear" type="fx_color_common" minOccurs="0"/>
                                        <xs:element name="depth_clear" type="float" minOccurs="0"/>
                                        <xs:element name="stencil_clear" type="xs:byte" minOccurs="0"/>
                                        <xs:element name="draw" type="fx_draw_common" minOccurs="0"/>
                                        <xs:choice minOccurs="0" maxOccurs="unbounded">
                                            <xs:group ref="gles_pipeline_settings"/>
                                        </xs:choice>
                                        <xs:element ref="extra" minOccurs="0" maxOccurs="unbounded"/>
                                    </xs:sequence>
                                    <xs:attribute name="sid" type="xs:NCName" use="optional">
                                        <xs:annotation>
                                            <xs:documentation>
                                            The sid attribute is a text string value containing the sub-identifier of this element.
                                            This value must be unique within the scope of the parent element. Optional attribute.
                                            </xs:documentation>
                                        </xs:annotation>
                                    </xs:attribute>
                                </xs:complexType>
                            </xs:element>
                            <xs:element ref="extra" minOccurs="0" maxOccurs="unbounded"/>
                        </xs:sequence>
                        <xs:attribute name="id" type="xs:ID"/>
                        <xs:attribute name="sid" type="xs:NCName" use="required">
                            <xs:annotation>
                                <xs:documentation>
                                The sid attribute is a text string value containing the sub-identifier of this element.
                                This value must be unique within the scope of the parent element.
                                </xs:documentation>
                            </xs:annotation>
                        </xs:attribute>
                    </xs:complexType>
                </xs:element>
                <xs:element ref="extra" minOccurs="0" maxOccurs="unbounded"/>
            </xs:sequence>
            <xs:attribute name="id" type="xs:ID" use="optional">
                <xs:annotation>
                    <xs:documentation>
                    The id attribute is a text string containing the unique identifier of this element.
                    This value must be unique within the instance document. Optional attribute.
                    </xs:documentation>
                </xs:annotation>
            </xs:attribute>
            <xs:attribute name="platform" type="xs:NCName" use="optional" default="PC">
                <xs:annotation>
                    <xs:documentation>
                    The type of platform. This is a vendor-defined character string that indicates the platform or capability target for the technique. Optional
                    </xs:documentation>
                </xs:annotation>
            </xs:attribute>
        </xs:complexType>
    </xs:element>
    <!-- COLLADA Physics -->
    <!-- new geometry types -->
    <xs:element name="box">
        <xs:annotation>
            <xs:documentation>
            An axis-aligned, centered box primitive.
            </xs:documentation>
        </xs:annotation>
        <xs:complexType>
            <xs:sequence>
                <xs:element name="half_extents" type="float3">
                    <xs:annotation>
                        <xs:documentation>
                        3 float values that represent the extents of the box
                        </xs:documentation>
                    </xs:annotation>
                </xs:element>
                <xs:element ref="extra" minOccurs="0" maxOccurs="unbounded">
                    <xs:annotation>
                        <xs:documentation>
                        The extra element may appear any number of times.
                        </xs:documentation>
                    </xs:annotation>
                </xs:element>
            </xs:sequence>
        </xs:complexType>
    </xs:element>
    <xs:element name="plane">
        <xs:annotation>
            <xs:documentation>
            An infinite plane primitive.
            </xs:documentation>
        </xs:annotation>
        <xs:complexType>
            <xs:sequence>
                <xs:element name="equation" type="float4">
                    <xs:annotation>
                        <xs:documentation>
                        4 float values that represent the coefficients for the plane’s equation:    Ax + By + Cz + D = 0
                        </xs:documentation>
                    </xs:annotation>
                </xs:element>
                <xs:element ref="extra" minOccurs="0" maxOccurs="unbounded">
                    <xs:annotation>
                        <xs:documentation>
                        The extra element may appear any number of times.
                        </xs:documentation>
                    </xs:annotation>
                </xs:element>
            </xs:sequence>
        </xs:complexType>
    </xs:element>
    <xs:element name="sphere">
        <xs:annotation>
            <xs:documentation>
            A centered sphere primitive.
            </xs:documentation>
        </xs:annotation>
        <xs:complexType>
            <xs:sequence>
                <xs:element name="radius" type="float">
                    <xs:annotation>
                        <xs:documentation>
                        A float value that represents the radius of the sphere
                        </xs:documentation>
                    </xs:annotation>
                </xs:element>
                <xs:element ref="extra" minOccurs="0" maxOccurs="unbounded">
                    <xs:annotation>
                        <xs:documentation>
                        The extra element may appear any number of times.
                        </xs:documentation>
                    </xs:annotation>
                </xs:element>
            </xs:sequence>
        </xs:complexType>
    </xs:element>
    <xs:element name="ellipsoid">
        <xs:complexType>
            <xs:sequence>
                <xs:element name="size" type="float3"/>
            </xs:sequence>
        </xs:complexType>
    </xs:element>
    <xs:element name="cylinder">
        <xs:annotation>
            <xs:documentation>
            A cylinder primitive that is centered on, and aligned with. the local Y axis.
            </xs:documentation>
        </xs:annotation>
        <xs:complexType>
            <xs:sequence>
                <xs:element name="height" type="float">
                    <xs:annotation>
                        <xs:documentation>
                        A float value that represents the length of the cylinder along the Y axis.
                        </xs:documentation>
                    </xs:annotation>
                </xs:element>
                <xs:element name="radius" type="float2">
                    <xs:annotation>
                        <xs:documentation>
                        float2 values that represent the radii of the cylinder.
                        </xs:documentation>
                    </xs:annotation>
                </xs:element>
                <xs:element ref="extra" minOccurs="0" maxOccurs="unbounded">
                    <xs:annotation>
                        <xs:documentation>
                        The extra element may appear any number of times.
                        </xs:documentation>
                    </xs:annotation>
                </xs:element>
            </xs:sequence>
        </xs:complexType>
    </xs:element>
    <xs:element name="tapered_cylinder">
        <xs:annotation>
            <xs:documentation>
            A tapered cylinder primitive that is centered on and aligned with the local Y axis.
            </xs:documentation>
        </xs:annotation>
        <xs:complexType>
            <xs:sequence>
                <xs:element name="height" type="float">
                    <xs:annotation>
                        <xs:documentation>
                        A float value that represents the length of the cylinder along the Y axis.
                        </xs:documentation>
                    </xs:annotation>
                </xs:element>
                <xs:element name="radius1" type="float2">
                    <xs:annotation>
                        <xs:documentation>
                        Two float values that represent the radii of the tapered cylinder at the positive (height/2)
                        Y value. Both ends of the tapered cylinder may be elliptical.
                        </xs:documentation>
                    </xs:annotation>
                </xs:element>
                <xs:element name="radius2" type="float2">
                    <xs:annotation>
                        <xs:documentation>
                        Two float values that represent the radii of the tapered cylinder at the negative (height/2)
                        Y value.Both ends of the tapered cylinder may be elliptical.
                        </xs:documentation>
                    </xs:annotation>
                </xs:element>
                <xs:element ref="extra" minOccurs="0" maxOccurs="unbounded">
                    <xs:annotation>
                        <xs:documentation>
                        The extra element may appear any number of times.
                        </xs:documentation>
                    </xs:annotation>
                </xs:element>
            </xs:sequence>
        </xs:complexType>
    </xs:element>
    <xs:element name="capsule">
        <xs:annotation>
            <xs:documentation>
            A capsule primitive that is centered on and aligned with the local Y axis.
            </xs:documentation>
        </xs:annotation>
        <xs:complexType>
            <xs:sequence>
                <xs:element name="height" type="float">
                    <xs:annotation>
                        <xs:documentation>
                        A float value that represents the length of the line segment connecting the centers
                        of the capping hemispheres.
                        </xs:documentation>
                    </xs:annotation>
                </xs:element>
                <xs:element name="radius" type="float2">
                    <xs:annotation>
                        <xs:documentation>
                        Two float values that represent the radii of the capsule (it may be elliptical)
                        </xs:documentation>
                    </xs:annotation>
                </xs:element>
                <xs:element ref="extra" minOccurs="0" maxOccurs="unbounded">
                    <xs:annotation>
                        <xs:documentation>
                        The extra element may appear any number of times.
                        </xs:documentation>
                    </xs:annotation>
                </xs:element>
            </xs:sequence>
        </xs:complexType>
    </xs:element>
    <xs:element name="tapered_capsule">
        <xs:annotation>
            <xs:documentation>
            A tapered capsule primitive that is centered on, and aligned with, the local Y axis.
            </xs:documentation>
        </xs:annotation>
        <xs:complexType>
            <xs:sequence>
                <xs:element name="height" type="float">
                    <xs:annotation>
                        <xs:documentation>
                        A float value that represents the length of the line segment connecting the centers of the
                        capping hemispheres.
                        </xs:documentation>
                    </xs:annotation>
                </xs:element>
                <xs:element name="radius1" type="float2">
                    <xs:annotation>
                        <xs:documentation>
                        Two float values that represent the radii of the tapered capsule at the positive (height/2)
                        Y value.Both ends of the tapered capsule may be elliptical.
                        </xs:documentation>
                    </xs:annotation>
                </xs:element>
                <xs:element name="radius2" type="float2">
                    <xs:annotation>
                        <xs:documentation>
                        Two float values that represent the radii of the tapered capsule at the negative (height/2)
                        Y value.Both ends of the tapered capsule may be elliptical.
                        </xs:documentation>
                    </xs:annotation>
                </xs:element>
                <xs:element ref="extra" minOccurs="0" maxOccurs="unbounded">
                    <xs:annotation>
                        <xs:documentation>
                        The extra element may appear any number of times.
                        </xs:documentation>
                    </xs:annotation>
                </xs:element>
            </xs:sequence>
        </xs:complexType>
    </xs:element>
    <xs:element name="convex_mesh">
        <xs:annotation>
            <xs:documentation>
            The definition of the convex_mesh element is identical to the mesh element with the exception that
            instead of a complete description (source, vertices, polygons etc.), it may simply point to another
            geometry to derive its shape. The latter case means that the convex hull of that geometry should
            be computed and is indicated by the optional “convex_hull_of” attribute.
            </xs:documentation>
        </xs:annotation>
        <xs:complexType>
            <xs:sequence minOccurs="0">
                <xs:element ref="source" maxOccurs="unbounded"/>
                <xs:element ref="vertices"/>
                <xs:choice minOccurs="0" maxOccurs="unbounded">
                    <xs:element ref="lines"/>
                    <xs:element ref="linestrips"/>
                    <xs:element ref="polygons"/>
                    <xs:element ref="polylist"/>
                    <xs:element ref="triangles"/>
                    <xs:element ref="trifans"/>
                    <xs:element ref="tristrips"/>
                </xs:choice>
                <xs:element ref="extra" minOccurs="0" maxOccurs="unbounded">
                    <xs:annotation>
                        <xs:documentation>
                        The extra element may appear any number of times.
                        </xs:documentation>
                    </xs:annotation>
                </xs:element>
            </xs:sequence>
            <xs:attribute name="convex_hull_of" type="xs:anyURI">
                <xs:annotation>
                    <xs:documentation>
                    The convex_hull_of attribute is a URI string of geometry to compute the convex hull of.
                    Optional attribute.
                    </xs:documentation>
                </xs:annotation>
            </xs:attribute>
        </xs:complexType>
    </xs:element>
    <!-- physics object elements -->
    <xs:element name="force_field">
        <xs:annotation>
            <xs:documentation>
            A general container for force-fields. At the moment, it only has techniques and extra elements.
            </xs:documentation>
        </xs:annotation>
        <xs:complexType>
            <xs:sequence>
                <xs:element ref="asset" minOccurs="0">
                    <xs:annotation>
                        <xs:documentation>
                        The force_field element may contain an asset element.
                        </xs:documentation>
                    </xs:annotation>
                </xs:element>
                <xs:element ref="technique" maxOccurs="unbounded">
                    <xs:annotation>
                        <xs:documentation>
                        This element must contain at least one non-common profile technique.
                        </xs:documentation>
                    </xs:annotation>
                </xs:element>
                <xs:element ref="extra" minOccurs="0" maxOccurs="unbounded">
                    <xs:annotation>
                        <xs:documentation>
                        The extra element may appear any number of times.
                        </xs:documentation>
                    </xs:annotation>
                </xs:element>
            </xs:sequence>
            <xs:attribute name="id" type="xs:ID">
                <xs:annotation>
                    <xs:documentation>
                    The id attribute is a text string containing the unique identifier of this element. This value
                    must be unique within the instance document. Optional attribute.
                    </xs:documentation>
                </xs:annotation>
            </xs:attribute>
            <xs:attribute name="name" type="xs:NCName">
                <xs:annotation>
                    <xs:documentation>
                    The name attribute is the text string name of this element. Optional attribute.
                    </xs:documentation>
                </xs:annotation>
            </xs:attribute>
        </xs:complexType>
    </xs:element>
    <xs:element name="physics_material">
        <xs:annotation>
            <xs:documentation>
            This element defines the physical properties of an object. It contains a technique/profile with
            parameters. The COMMON profile defines the built-in names, such as static_friction.
            </xs:documentation>
        </xs:annotation>
        <xs:complexType>
            <xs:sequence>
                <xs:element ref="asset" minOccurs="0">
                    <xs:annotation>
                        <xs:documentation>
                        The physics_material element may contain an asset element.
                        </xs:documentation>
                    </xs:annotation>
                </xs:element>
                <xs:element name="technique_common">
                    <xs:annotation>
                        <xs:documentation>
                        The technique_common element specifies the physics_material information for the common profile
                        which all COLLADA implementations need to support.
                        </xs:documentation>
                    </xs:annotation>
                    <xs:complexType>
                        <xs:sequence>
                            <xs:element name="dynamic_friction" type="TargetableFloat" minOccurs="0">
                                <xs:annotation>
                                    <xs:documentation>
                                    Dynamic friction coefficient
                                    </xs:documentation>
                                </xs:annotation>
                            </xs:element>
                            <xs:element name="restitution" type="TargetableFloat" minOccurs="0">
                                <xs:annotation>
                                    <xs:documentation>
                                    The proportion of the kinetic energy preserved in the impact (typically ranges from 0.0 to 1.0)
                                    </xs:documentation>
                                </xs:annotation>
                            </xs:element>
                            <xs:element name="static_friction" type="TargetableFloat" minOccurs="0">
                                <xs:annotation>
                                    <xs:documentation>
                                    Static friction coefficient
                                    </xs:documentation>
                                </xs:annotation>
                            </xs:element>
                        </xs:sequence>
                    </xs:complexType>
                </xs:element>
                <xs:element ref="technique" minOccurs="0" maxOccurs="unbounded">
                    <xs:annotation>
                        <xs:documentation>
                        This element may contain any number of non-common profile techniques.
                        </xs:documentation>
                    </xs:annotation>
                </xs:element>
                <xs:element ref="extra" minOccurs="0" maxOccurs="unbounded">
                    <xs:annotation>
                        <xs:documentation>
                        The extra element may appear any number of times.
                        </xs:documentation>
                    </xs:annotation>
                </xs:element>
            </xs:sequence>
            <xs:attribute name="id" type="xs:ID">
                <xs:annotation>
                    <xs:documentation>
                    The id attribute is a text string containing the unique identifier of this element.
                    This value must be unique within the instance document. Optional attribute.
                    </xs:documentation>
                </xs:annotation>
            </xs:attribute>
            <xs:attribute name="name" type="xs:NCName">
                <xs:annotation>
                    <xs:documentation>
                    The name attribute is the text string name of this element. Optional attribute.
                    </xs:documentation>
                </xs:annotation>
            </xs:attribute>
        </xs:complexType>
    </xs:element>
    <xs:element name="physics_scene">
        <xs:complexType>
            <xs:sequence>
                <xs:element ref="asset" minOccurs="0">
                    <xs:annotation>
                        <xs:documentation>
                        The physics_scene element may contain an asset element.
                        </xs:documentation>
                    </xs:annotation>
                </xs:element>
                <xs:element ref="instance_force_field" minOccurs="0" maxOccurs="unbounded">
                    <xs:annotation>
                        <xs:documentation>
                        There may be any number of instance_force_field elements.
                        </xs:documentation>
                    </xs:annotation>
                </xs:element>
                <xs:element ref="instance_physics_model" minOccurs="0" maxOccurs="unbounded">
                    <xs:annotation>
                        <xs:documentation>
                        There may be any number of instance_physics_model elements.
                        </xs:documentation>
                    </xs:annotation>
                </xs:element>
                <xs:element name="technique_common">
                    <xs:annotation>
                        <xs:documentation>
                        The technique_common element specifies the physics_scene information for the common profile
                        which all COLLADA implementations need to support.
                        </xs:documentation>
                    </xs:annotation>
                    <xs:complexType>
                        <xs:sequence>
                            <xs:element name="gravity" type="TargetableFloat3" minOccurs="0">
                                <xs:annotation>
                                    <xs:documentation>
                                    The gravity vector to use for the physics_scene.
                                    </xs:documentation>
                                </xs:annotation>
                            </xs:element>
                            <xs:element name="time_step" type="TargetableFloat" minOccurs="0">
                                <xs:annotation>
                                    <xs:documentation>
                                    The time_step for the physics_scene.
                                    </xs:documentation>
                                </xs:annotation>
                            </xs:element>
                        </xs:sequence>
                    </xs:complexType>
                </xs:element>
                <xs:element ref="technique" minOccurs="0" maxOccurs="unbounded">
                    <xs:annotation>
                        <xs:documentation>
                        This element may contain any number of non-common profile techniques.
                        </xs:documentation>
                    </xs:annotation>
                </xs:element>
                <xs:element ref="extra" minOccurs="0" maxOccurs="unbounded">
                    <xs:annotation>
                        <xs:documentation>
                        The extra element may appear any number of times.
                        </xs:documentation>
                    </xs:annotation>
                </xs:element>
            </xs:sequence>
            <xs:attribute name="id" type="xs:ID">
                <xs:annotation>
                    <xs:documentation>
                    The id attribute is a text string containing the unique identifier of this element.
                    This value must be unique within the instance document. Optional attribute.
                    </xs:documentation>
                </xs:annotation>
            </xs:attribute>
            <xs:attribute name="name" type="xs:NCName">
                <xs:annotation>
                    <xs:documentation>
                    The name attribute is the text string name of this element. Optional attribute.
                    </xs:documentation>
                </xs:annotation>
            </xs:attribute>
        </xs:complexType>
    </xs:element>
    <xs:simpleType name="SpringType">
        <xs:restriction base="xs:NMTOKEN">
            <xs:enumeration value="LINEAR"/>
            <xs:enumeration value="ANGULAR"/>
        </xs:restriction>
    </xs:simpleType>
    <xs:element name="rigid_body">
        <xs:annotation>
            <xs:documentation>
            This element allows for describing simulated bodies that do not deform. These bodies may or may
            not be connected by constraints (hinge, ball-joint etc.).  Rigid-bodies, constraints etc. are
            encapsulated in physics_model elements to allow for instantiating complex models.
            </xs:documentation>
        </xs:annotation>
        <xs:complexType>
            <xs:sequence>
                <xs:element name="technique_common">
                    <xs:annotation>
                        <xs:documentation>
                        The technique_common element specifies the rigid_body information for the common profile which all
                        COLLADA implementations need to support.
                        </xs:documentation>
                    </xs:annotation>
                    <xs:complexType>
                        <xs:sequence>
                            <xs:element name="dynamic" minOccurs="0">
                                <xs:annotation>
                                    <xs:documentation>
                                    If false, the rigid_body is not moveable
                                    </xs:documentation>
                                </xs:annotation>
                                <xs:complexType>
                                    <xs:simpleContent>
                                        <xs:extension base="bool">
                                            <xs:attribute name="sid" type="xs:NCName">
                                                <xs:annotation>
                                                    <xs:documentation>
                                                    The sid attribute is a text string value containing the sub-identifier of this element.
                                                    This value must be unique within the scope of the parent element. Optional attribute.
                                                    </xs:documentation>
                                                </xs:annotation>
                                            </xs:attribute>
                                        </xs:extension>
                                    </xs:simpleContent>
                                </xs:complexType>
                            </xs:element>
                            <xs:element name="mass" type="TargetableFloat" minOccurs="0">
                                <xs:annotation>
                                    <xs:documentation>
                                    The total mass of the rigid-body
                                    </xs:documentation>
                                </xs:annotation>
                            </xs:element>
                            <xs:element name="mass_frame" minOccurs="0">
                                <xs:annotation>
                                    <xs:documentation>
                                    Defines the center and orientation of mass of the rigid-body relative to the local origin of the
                                    “root” shape.This makes the off-diagonal elements of the inertia tensor (products of inertia) all
                                    0 and allows us to just store the diagonal elements (moments of inertia).
                                    </xs:documentation>
                                </xs:annotation>
                                <xs:complexType>
                                    <xs:choice maxOccurs="unbounded">
                                        <xs:element ref="translate"/>
                                        <xs:element ref="rotate"/>
                                    </xs:choice>
                                </xs:complexType>
                            </xs:element>
                            <xs:element name="inertia" type="TargetableFloat3" minOccurs="0">
                                <xs:annotation>
                                    <xs:documentation>
                                    float3 – The diagonal elements of the inertia tensor (moments of inertia), which is represented
                                    in the local frame of the center of mass. See above.
                                    </xs:documentation>
                                </xs:annotation>
                            </xs:element>
                            <xs:choice minOccurs="0">
                                <xs:element ref="instance_physics_material">
                                    <xs:annotation>
                                        <xs:documentation>
                                        References a physics_material for the rigid_body.
                                        </xs:documentation>
                                    </xs:annotation>
                                </xs:element>
                                <xs:element ref="physics_material">
                                    <xs:annotation>
                                        <xs:documentation>
                                        Defines a physics_material for the rigid_body.
                                        </xs:documentation>
                                    </xs:annotation>
                                </xs:element>
                            </xs:choice>
                            <xs:element name="shape" maxOccurs="unbounded">
                                <xs:annotation>
                                    <xs:documentation>
                                    This element allows for describing components of a rigid_body.
                                    </xs:documentation>
                                </xs:annotation>
                                <xs:complexType>
                                    <xs:sequence>
                                        <xs:element name="hollow" minOccurs="0">
                                            <xs:annotation>
                                                <xs:documentation>
                                                If true, the mass is distributed along the surface of the shape
                                                </xs:documentation>
                                            </xs:annotation>
                                            <xs:complexType>
                                                <xs:simpleContent>
                                                    <xs:extension base="bool">
                                                        <xs:attribute name="sid" type="xs:NCName">
                                                            <xs:annotation>
                                                                <xs:documentation>
                                                                The sid attribute is a text string value containing the sub-identifier of this element.
                                                                This value must be unique within the scope of the parent element. Optional attribute.
                                                                </xs:documentation>
                                                            </xs:annotation>
                                                        </xs:attribute>
                                                    </xs:extension>
                                                </xs:simpleContent>
                                            </xs:complexType>
                                        </xs:element>
                                        <xs:element name="mass" type="TargetableFloat" minOccurs="0">
                                            <xs:annotation>
                                                <xs:documentation>
                                                The mass of the shape.
                                                </xs:documentation>
                                            </xs:annotation>
                                        </xs:element>
                                        <xs:element name="density" type="TargetableFloat" minOccurs="0">
                                            <xs:annotation>
                                                <xs:documentation>
                                                The density of the shape.
                                                </xs:documentation>
                                            </xs:annotation>
                                        </xs:element>
                                        <xs:choice minOccurs="0">
                                            <xs:element ref="instance_physics_material">
                                                <xs:annotation>
                                                    <xs:documentation>
                                                    References a physics_material for the shape.
                                                    </xs:documentation>
                                                </xs:annotation>
                                            </xs:element>
                                            <xs:element ref="physics_material">
                                                <xs:annotation>
                                                    <xs:documentation>
                                                    Defines a physics_material for the shape.
                                                    </xs:documentation>
                                                </xs:annotation>
                                            </xs:element>
                                        </xs:choice>
                                        <xs:choice>
                                            <xs:element ref="instance_geometry">
                                                <xs:annotation>
                                                    <xs:documentation>
                                                    Instances a geometry to use to define this shape.
                                                    </xs:documentation>
                                                </xs:annotation>
                                            </xs:element>
                                            <xs:element ref="plane">
                                                <xs:annotation>
                                                    <xs:documentation>
                                                    Defines a plane to use for this shape.
                                                    </xs:documentation>
                                                </xs:annotation>
                                            </xs:element>
                                            <xs:element ref="box">
                                                <xs:annotation>
                                                    <xs:documentation>
                                                    Defines a box to use for this shape.
                                                    </xs:documentation>
                                                </xs:annotation>
                                            </xs:element>
                                            <xs:element ref="sphere">
                                                <xs:annotation>
                                                    <xs:documentation>
                                                    Defines a sphere to use for this shape.
                                                    </xs:documentation>
                                                </xs:annotation>
                                            </xs:element>
                                            <xs:element ref="cylinder">
                                                <xs:annotation>
                                                    <xs:documentation>
                                                    Defines a cyliner to use for this shape.
                                                    </xs:documentation>
                                                </xs:annotation>
                                            </xs:element>
                                            <xs:element ref="tapered_cylinder">
                                                <xs:annotation>
                                                    <xs:documentation>
                                                    Defines a tapered_cylinder to use for this shape.
                                                    </xs:documentation>
                                                </xs:annotation>
                                            </xs:element>
                                            <xs:element ref="capsule">
                                                <xs:annotation>
                                                    <xs:documentation>
                                                    Defines a capsule to use for this shape.
                                                    </xs:documentation>
                                                </xs:annotation>
                                            </xs:element>
                                            <xs:element ref="tapered_capsule">
                                                <xs:annotation>
                                                    <xs:documentation>
                                                    Defines a tapered_capsule to use for this shape.
                                                    </xs:documentation>
                                                </xs:annotation>
                                            </xs:element>
                                        </xs:choice>
                                        <xs:choice minOccurs="0" maxOccurs="unbounded">
                                            <xs:element ref="translate">
                                                <xs:annotation>
                                                    <xs:documentation>
                                                    Allows a tranformation for the shape.
                                                    </xs:documentation>
                                                </xs:annotation>
                                            </xs:element>
                                            <xs:element ref="rotate">
                                                <xs:annotation>
                                                    <xs:documentation>
                                                    Allows a tranformation for the shape.
                                                    </xs:documentation>
                                                </xs:annotation>
                                            </xs:element>
                                        </xs:choice>
                                        <xs:element ref="extra" minOccurs="0" maxOccurs="unbounded">
                                            <xs:annotation>
                                                <xs:documentation>
                                                The extra element may appear any number of times.
                                                </xs:documentation>
                                            </xs:annotation>
                                        </xs:element>
                                    </xs:sequence>
                                </xs:complexType>
                            </xs:element>
                        </xs:sequence>
                    </xs:complexType>
                </xs:element>
                <xs:element ref="technique" minOccurs="0" maxOccurs="unbounded">
                    <xs:annotation>
                        <xs:documentation>
                        This element may contain any number of non-common profile techniques.
                        </xs:documentation>
                    </xs:annotation>
                </xs:element>
                <xs:element ref="extra" minOccurs="0" maxOccurs="unbounded">
                    <xs:annotation>
                        <xs:documentation>
                        The extra element may appear any number of times.
                        </xs:documentation>
                    </xs:annotation>
                </xs:element>
            </xs:sequence>
            <xs:attribute name="sid" type="xs:NCName" use="required">
                <xs:annotation>
                    <xs:documentation>
                    The sid attribute is a text string value containing the sub-identifier of this element. This
                    value must be unique within the scope of the parent element. Optional attribute.
                    </xs:documentation>
                </xs:annotation>
            </xs:attribute>
            <xs:attribute name="name" type="xs:NCName">
                <xs:annotation>
                    <xs:documentation>
                    The name attribute is the text string name of this element. Optional attribute.
                    </xs:documentation>
                </xs:annotation>
            </xs:attribute>
        </xs:complexType>
    </xs:element>
    <xs:element name="rigid_constraint">
        <xs:annotation>
            <xs:documentation>
            This element allows for connecting components, such as rigid_body into complex physics models
            with moveable parts.
            </xs:documentation>
        </xs:annotation>
        <xs:complexType>
            <xs:sequence>
                <xs:element name="ref_attachment">
                    <xs:annotation>
                        <xs:documentation>
                        Defines the attachment (to a rigid_body or a node) to be used as the reference-frame.
                        </xs:documentation>
                    </xs:annotation>
                    <xs:complexType>
                        <xs:choice minOccurs="0" maxOccurs="unbounded">
                            <xs:element ref="translate">
                                <xs:annotation>
                                    <xs:documentation>
                                    Allows you to "position" the attachment point.
                                    </xs:documentation>
                                </xs:annotation>
                            </xs:element>
                            <xs:element ref="rotate">
                                <xs:annotation>
                                    <xs:documentation>
                                    Allows you to "position" the attachment point.
                                    </xs:documentation>
                                </xs:annotation>
                            </xs:element>
                            <xs:element ref="extra" minOccurs="0" maxOccurs="unbounded">
                                <xs:annotation>
                                    <xs:documentation>
                                    The extra element may appear any number of times.
                                    </xs:documentation>
                                </xs:annotation>
                            </xs:element>
                        </xs:choice>
                        <xs:attribute name="rigid_body" type="xs:anyURI">
                            <xs:annotation>
                                <xs:documentation>
                                The “rigid_body” attribute is a relative reference to a rigid-body within the same
                                physics_model.
                                </xs:documentation>
                            </xs:annotation>
                        </xs:attribute>
                    </xs:complexType>
                </xs:element>
                <xs:element name="attachment">
                    <xs:annotation>
                        <xs:documentation>
                        Defines an attachment to a rigid-body or a node.
                        </xs:documentation>
                    </xs:annotation>
                    <xs:complexType>
                        <xs:choice minOccurs="0" maxOccurs="unbounded">
                            <xs:element ref="translate">
                                <xs:annotation>
                                    <xs:documentation>
                                    Allows you to "position" the attachment point.
                                    </xs:documentation>
                                </xs:annotation>
                            </xs:element>
                            <xs:element ref="rotate">
                                <xs:annotation>
                                    <xs:documentation>
                                    Allows you to "position" the attachment point.
                                    </xs:documentation>
                                </xs:annotation>
                            </xs:element>
                            <xs:element ref="extra" minOccurs="0" maxOccurs="unbounded">
                                <xs:annotation>
                                    <xs:documentation>
                                    The extra element may appear any number of times.
                                    </xs:documentation>
                                </xs:annotation>
                            </xs:element>
                        </xs:choice>
                        <xs:attribute name="rigid_body" type="xs:anyURI">
                            <xs:annotation>
                                <xs:documentation>
                                The “rigid_body” attribute is a relative reference to a rigid-body within the same physics_model.
                                </xs:documentation>
                            </xs:annotation>
                        </xs:attribute>
                    </xs:complexType>
                </xs:element>
                <xs:element name="technique_common">
                    <xs:annotation>
                        <xs:documentation>
                        The technique_common element specifies the rigid_constraint information for the common profile
                        which all COLLADA implementations need to support.
                        </xs:documentation>
                    </xs:annotation>
                    <xs:complexType>
                        <xs:sequence>
                            <xs:element name="enabled" default="true" minOccurs="0">
                                <xs:annotation>
                                    <xs:documentation>
                                    If false, the constraint doesn’t exert any force or influence on the rigid bodies.
                                    </xs:documentation>
                                </xs:annotation>
                                <xs:complexType>
                                    <xs:simpleContent>
                                        <xs:extension base="bool">
                                            <xs:attribute name="sid" type="xs:NCName">
                                                <xs:annotation>
                                                    <xs:documentation>
                                                    The sid attribute is a text string value containing the sub-identifier of this element.
                                                    This value must be unique within the scope of the parent element. Optional attribute.
                                                    </xs:documentation>
                                                </xs:annotation>
                                            </xs:attribute>
                                        </xs:extension>
                                    </xs:simpleContent>
                                </xs:complexType>
                            </xs:element>
                            <xs:element name="interpenetrate" default="false" minOccurs="0">
                                <xs:annotation>
                                    <xs:documentation>
                                    Indicates whether the attached rigid bodies may inter-penetrate.
                                    </xs:documentation>
                                </xs:annotation>
                                <xs:complexType>
                                    <xs:simpleContent>
                                        <xs:extension base="bool">
                                            <xs:attribute name="sid" type="xs:NCName">
                                                <xs:annotation>
                                                    <xs:documentation>
                                                    The sid attribute is a text string value containing the sub-identifier of this element.
                                                    This value must be unique within the scope of the parent element. Optional attribute.
                                                    </xs:documentation>
                                                </xs:annotation>
                                            </xs:attribute>
                                        </xs:extension>
                                    </xs:simpleContent>
                                </xs:complexType>
                            </xs:element>
                            <xs:element name="limits" minOccurs="0">
                                <xs:annotation>
                                    <xs:documentation>
                                    The limits element provides a flexible way to specify the constraint limits (degrees of freedom
                                    and ranges).
                                    </xs:documentation>
                                </xs:annotation>
                                <xs:complexType>
                                    <xs:sequence>
                                        <xs:element name="swing_cone_and_twist" minOccurs="0">
                                            <xs:annotation>
                                                <xs:documentation>
                                                The swing_cone_and_twist element describes the angular limits along each rotation axis in degrees.
                                                The the X and Y limits describe a “swing cone” and the Z limits describe the “twist angle” range
                                                </xs:documentation>
                                            </xs:annotation>
                                            <xs:complexType>
                                                <xs:sequence>
                                                    <xs:element name="min" type="TargetableFloat3" default="0.0 0.0 0.0" minOccurs="0">
                                                        <xs:annotation>
                                                            <xs:documentation>
                                                            The minimum values for the limit.
                                                            </xs:documentation>
                                                        </xs:annotation>
                                                    </xs:element>
                                                    <xs:element name="max" type="TargetableFloat3" default="0.0 0.0 0.0" minOccurs="0">
                                                        <xs:annotation>
                                                            <xs:documentation>
                                                            The maximum values for the limit.
                                                            </xs:documentation>
                                                        </xs:annotation>
                                                    </xs:element>
                                                </xs:sequence>
                                            </xs:complexType>
                                        </xs:element>
                                        <xs:element name="linear" minOccurs="0">
                                            <xs:annotation>
                                                <xs:documentation>
                                                The linear element describes linear (translational) limits along each axis.
                                                </xs:documentation>
                                            </xs:annotation>
                                            <xs:complexType>
                                                <xs:sequence>
                                                    <xs:element name="min" type="TargetableFloat3" default="0.0 0.0 0.0" minOccurs="0">
                                                        <xs:annotation>
                                                            <xs:documentation>
                                                            The minimum values for the limit.
                                                            </xs:documentation>
                                                        </xs:annotation>
                                                    </xs:element>
                                                    <xs:element name="max" type="TargetableFloat3" default="0.0 0.0 0.0" minOccurs="0">
                                                        <xs:annotation>
                                                            <xs:documentation>
                                                            The maximum values for the limit.
                                                            </xs:documentation>
                                                        </xs:annotation>
                                                    </xs:element>
                                                </xs:sequence>
                                            </xs:complexType>
                                        </xs:element>
                                    </xs:sequence>
                                </xs:complexType>
                            </xs:element>
                            <xs:element name="spring" minOccurs="0">
                                <xs:annotation>
                                    <xs:documentation>
                                    Spring, based on distance (“LINEAR”) or angle (“ANGULAR”).
                                    </xs:documentation>
                                </xs:annotation>
                                <xs:complexType>
                                    <xs:sequence>
                                        <xs:element name="angular" minOccurs="0">
                                            <xs:annotation>
                                                <xs:documentation>
                                                The angular spring properties.
                                                </xs:documentation>
                                            </xs:annotation>
                                            <xs:complexType>
                                                <xs:sequence>
                                                    <xs:element name="stiffness" type="TargetableFloat" default="1.0" minOccurs="0">
                                                        <xs:annotation>
                                                            <xs:documentation>
                                                            The stiffness (also called spring coefficient) has units of force/angle in degrees.
                                                            </xs:documentation>
                                                        </xs:annotation>
                                                    </xs:element>
                                                    <xs:element name="damping" type="TargetableFloat" default="0.0" minOccurs="0">
                                                        <xs:annotation>
                                                            <xs:documentation>
                                                            The spring damping coefficient.
                                                            </xs:documentation>
                                                        </xs:annotation>
                                                    </xs:element>
                                                    <xs:element name="target_value" type="TargetableFloat" default="0.0" minOccurs="0">
                                                        <xs:annotation>
                                                            <xs:documentation>
                                                            The spring's target or resting distance.
                                                            </xs:documentation>
                                                        </xs:annotation>
                                                    </xs:element>
                                                </xs:sequence>
                                            </xs:complexType>
                                        </xs:element>
                                        <xs:element name="linear" minOccurs="0">
                                            <xs:annotation>
                                                <xs:documentation>
                                                The linear spring properties.
                                                </xs:documentation>
                                            </xs:annotation>
                                            <xs:complexType>
                                                <xs:sequence>
                                                    <xs:element name="stiffness" type="TargetableFloat" default="1.0" minOccurs="0">
                                                        <xs:annotation>
                                                            <xs:documentation>
                                                            The stiffness (also called spring coefficient) has units of force/distance.
                                                            </xs:documentation>
                                                        </xs:annotation>
                                                    </xs:element>
                                                    <xs:element name="damping" type="TargetableFloat" default="0.0" minOccurs="0">
                                                        <xs:annotation>
                                                            <xs:documentation>
                                                            The spring damping coefficient.
                                                            </xs:documentation>
                                                        </xs:annotation>
                                                    </xs:element>
                                                    <xs:element name="target_value" type="TargetableFloat" default="0.0" minOccurs="0">
                                                        <xs:annotation>
                                                            <xs:documentation>
                                                            The spring's target or resting distance.
                                                            </xs:documentation>
                                                        </xs:annotation>
                                                    </xs:element>
                                                </xs:sequence>
                                            </xs:complexType>
                                        </xs:element>
                                    </xs:sequence>
                                </xs:complexType>
                            </xs:element>
                        </xs:sequence>
                    </xs:complexType>
                </xs:element>
                <xs:element ref="technique" minOccurs="0" maxOccurs="unbounded">
                    <xs:annotation>
                        <xs:documentation>
                        This element may contain any number of non-common profile techniques.
                        </xs:documentation>
                    </xs:annotation>
                </xs:element>
                <xs:element ref="extra" minOccurs="0" maxOccurs="unbounded">
                    <xs:annotation>
                        <xs:documentation>
                        The extra element may appear any number of times.
                        </xs:documentation>
                    </xs:annotation>
                </xs:element>
            </xs:sequence>
            <xs:attribute name="sid" type="xs:NCName" use="required">
                <xs:annotation>
                    <xs:documentation>
                    The sid attribute is a text string value containing the sub-identifier of this element.
                    This value must be unique within the scope of the parent element. Optional attribute.
                    </xs:documentation>
                </xs:annotation>
            </xs:attribute>
            <xs:attribute name="name" type="xs:NCName">
                <xs:annotation>
                    <xs:documentation>
                    The name attribute is the text string name of this element. Optional attribute.
                    </xs:documentation>
                </xs:annotation>
            </xs:attribute>
        </xs:complexType>
    </xs:element>
    <xs:element name="physics_model">
        <xs:annotation>
            <xs:documentation>
            This element allows for building complex combinations of rigid-bodies and constraints that
            may be instantiated multiple times.
            </xs:documentation>
        </xs:annotation>
        <xs:complexType>
            <xs:sequence>
                <xs:element ref="asset" minOccurs="0">
                    <xs:annotation>
                        <xs:documentation>
                        The physics_model element may contain an asset element.
                        </xs:documentation>
                    </xs:annotation>
                </xs:element>
                <xs:element ref="rigid_body" minOccurs="0" maxOccurs="unbounded">
                    <xs:annotation>
                        <xs:documentation>
                        The physics_model may define any number of rigid_body elements.
                        </xs:documentation>
                    </xs:annotation>
                </xs:element>
                <xs:element ref="rigid_constraint" minOccurs="0" maxOccurs="unbounded">
                    <xs:annotation>
                        <xs:documentation>
                        The physics_model may define any number of rigid_constraint elements.
                        </xs:documentation>
                    </xs:annotation>
                </xs:element>
                <xs:element ref="instance_physics_model" minOccurs="0" maxOccurs="unbounded">
                    <xs:annotation>
                        <xs:documentation>
                        The physics_model may instance any number of other physics_model elements.
                        </xs:documentation>
                    </xs:annotation>
                </xs:element>
                <xs:element ref="extra" minOccurs="0" maxOccurs="unbounded">
                    <xs:annotation>
                        <xs:documentation>
                        The extra element may appear any number of times.
                        </xs:documentation>
                    </xs:annotation>
                </xs:element>
            </xs:sequence>
            <xs:attribute name="id" type="xs:ID">
                <xs:annotation>
                    <xs:documentation>
                    The id attribute is a text string containing the unique identifier of this element.
                    This value must be unique within the instance document. Optional attribute.
                    </xs:documentation>
                </xs:annotation>
            </xs:attribute>
            <xs:attribute name="name" type="xs:NCName">
                <xs:annotation>
                    <xs:documentation>
                    The name attribute is the text string name of this element. Optional attribute.
                    </xs:documentation>
                </xs:annotation>
            </xs:attribute>
        </xs:complexType>
    </xs:element>
    <!-- COMMON Profile Types -->
    <xs:simpleType name="Common_profile_input">
        <xs:annotation>
            <xs:appinfo>constant-strings</xs:appinfo>
        </xs:annotation>
        <xs:restriction base="xs:NMTOKEN">
            <xs:enumeration value="BINORMAL"/>
            <xs:enumeration value="COLOR"/>
            <xs:enumeration value="CONTINUITY"/>
            <xs:enumeration value="IMAGE"/>
            <xs:enumeration value="IN_TANGENT"/>
            <xs:enumeration value="INPUT"/>
            <xs:enumeration value="INTERPOLATION"/>
            <xs:enumeration value="INV_BIND_MATRIX"/>
            <xs:enumeration value="JOINT"/>
            <xs:enumeration value="LINEAR_STEPS"/>
            <xs:enumeration value="MORPH_TARGET"/>
            <xs:enumeration value="MORPH_WEIGHT"/>
            <xs:enumeration value="NORMAL"/>
            <xs:enumeration value="OUTPUT"/>
            <xs:enumeration value="OUT_TANGENT"/>
            <xs:enumeration value="POSITION"/>
            <xs:enumeration value="TANGENT"/>
            <xs:enumeration value="TEXBINORMAL"/>
            <xs:enumeration value="TEXCOORD"/>
            <xs:enumeration value="TEXTANGENT"/>
            <xs:enumeration value="UV"/>
            <xs:enumeration value="VERTEX"/>
            <xs:enumeration value="WEIGHT"/>
        </xs:restriction>
    </xs:simpleType>
    <xs:simpleType name="Common_profile_param">
        <xs:annotation>
            <xs:appinfo>constant-strings</xs:appinfo>
        </xs:annotation>
        <xs:restriction base="xs:NMTOKEN">
            <xs:enumeration value="A"/>
            <xs:enumeration value="ANGLE"/>
            <xs:enumeration value="B"/>
            <xs:enumeration value="DOUBLE_SIDED"/>
            <xs:enumeration value="G"/>
            <xs:enumeration value="P"/>
            <xs:enumeration value="Q"/>
            <xs:enumeration value="R"/>
            <xs:enumeration value="S"/>
            <xs:enumeration value="T"/>
            <xs:enumeration value="TIME"/>
            <xs:enumeration value="U"/>
            <xs:enumeration value="V"/>
            <xs:enumeration value="W"/>
            <xs:enumeration value="X"/>
            <xs:enumeration value="Y"/>
            <xs:enumeration value="Z"/>
        </xs:restriction>
    </xs:simpleType>
</xs:schema>"""

XML_XSD = """<?xml version='1.0'?>
<!DOCTYPE xs:schema PUBLIC "-//W3C//DTD XMLSCHEMA 200102//EN" "XMLSchema.dtd" >
<xs:schema targetNamespace="http://www.w3.org/XML/1998/namespace" xmlns:xs="http://www.w3.org/2001/XMLSchema" xml:lang="en">

 <xs:annotation>
  <xs:documentation>
   See http://www.w3.org/XML/1998/namespace.html and
   http://www.w3.org/TR/REC-xml for information about this namespace.

    This schema document describes the XML namespace, in a form
    suitable for import by other schema documents.

    Note that local names in this namespace are intended to be defined
    only by the World Wide Web Consortium or its subgroups.  The
    following names are currently defined in this namespace and should
    not be used with conflicting semantics by any Working Group,
    specification, or document instance:

    base (as an attribute name): denotes an attribute whose value
         provides a URI to be used as the base for interpreting any
         relative URIs in the scope of the element on which it
         appears; its value is inherited.  This name is reserved
         by virtue of its definition in the XML Base specification.

    lang (as an attribute name): denotes an attribute whose value
         is a language code for the natural language of the content of
         any element; its value is inherited.  This name is reserved
         by virtue of its definition in the XML specification.

    space (as an attribute name): denotes an attribute whose
         value is a keyword indicating what whitespace processing
         discipline is intended for the content of the element; its
         value is inherited.  This name is reserved by virtue of its
         definition in the XML specification.

    Father (in any context at all): denotes Jon Bosak, the chair of
         the original XML Working Group.  This name is reserved by
         the following decision of the W3C XML Plenary and
         XML Coordination groups:

             In appreciation for his vision, leadership and dedication
             the W3C XML Plenary on this 10th day of February, 2000
             reserves for Jon Bosak in perpetuity the XML name
             xml:Father
  </xs:documentation>
 </xs:annotation>

 <xs:annotation>
  <xs:documentation>This schema defines attributes and an attribute group
        suitable for use by
        schemas wishing to allow xml:base, xml:lang or xml:space attributes
        on elements they define.

        To enable this, such a schema must import this schema
        for the XML namespace, e.g. as follows:
        &lt;schema . . .>
         . . .
         &lt;import namespace="http://www.w3.org/XML/1998/namespace"
                    schemaLocation="http://www.w3.org/2001/03/xml.xsd"/>

        Subsequently, qualified reference to any of the attributes
        or the group defined below will have the desired effect, e.g.

        &lt;type . . .>
         . . .
         &lt;attributeGroup ref="xml:specialAttrs"/>

         will define a type which will schema-validate an instance
         element with any of those attributes</xs:documentation>
 </xs:annotation>

 <xs:annotation>
  <xs:documentation>In keeping with the XML Schema WG's standard versioning
   policy, this schema document will persist at
   http://www.w3.org/2001/03/xml.xsd.
   At the date of issue it can also be found at
   http://www.w3.org/2001/xml.xsd.
   The schema document at that URI may however change in the future,
   in order to remain compatible with the latest version of XML Schema
   itself.  In other words, if the XML Schema namespace changes, the version
   of this document at
   http://www.w3.org/2001/xml.xsd will change
   accordingly; the version at
   http://www.w3.org/2001/03/xml.xsd will not change.
  </xs:documentation>
 </xs:annotation>

 <xs:attribute name="lang" type="xs:language">
  <xs:annotation>
   <xs:documentation>In due course, we should install the relevant ISO 2- and 3-letter
         codes as the enumerated possible values . . .</xs:documentation>
  </xs:annotation>
 </xs:attribute>

 <xs:attribute name="space" default="preserve">
  <xs:simpleType>
   <xs:restriction base="xs:NCName">
    <xs:enumeration value="default"/>
    <xs:enumeration value="preserve"/>
   </xs:restriction>
  </xs:simpleType>
 </xs:attribute>

 <xs:attribute name="base" type="xs:anyURI">
  <xs:annotation>
   <xs:documentation>See http://www.w3.org/TR/xmlbase/ for
                     information about this attribute.</xs:documentation>
  </xs:annotation>
 </xs:attribute>

 <xs:attributeGroup name="specialAttrs">
  <xs:attribute ref="xml:base"/>
  <xs:attribute ref="xml:lang"/>
  <xs:attribute ref="xml:space"/>
 </xs:attributeGroup>

</xs:schema>
"""

class ColladaResolver(lxml.etree.Resolver):
    """COLLADA XML Resolver. If a known URL referenced
    from the COLLADA spec is resolved, a cached local
    copy is returned instead of initiating a network
    request"""
    def resolve(self, url, id, context):
        """Currently Resolves:
         * http://www.w3.org/2001/03/xml.xsd
        """
        if url == 'http://www.w3.org/2001/03/xml.xsd':
            return self.resolve_string(XML_XSD, context)
        else:
            return None


class ColladaValidator(object):
    """Validates a collada lxml document"""

    def __init__(self):
        """Initializes the validator"""
        self.COLLADA_SCHEMA_1_4_1_DOC = None
        self._COLLADA_SCHEMA_1_4_1_INSTANCE = None

    def _getColladaSchemaInstance(self):
        if self._COLLADA_SCHEMA_1_4_1_INSTANCE is None:
            self._parser = lxml.etree.XMLParser()
            self._parser.resolvers.add(ColladaResolver())
            self.COLLADA_SCHEMA_1_4_1_DOC = lxml.etree.parse(
                    BytesIO(bytes(COLLADA_SCHEMA_1_4_1, encoding='utf-8')),
                    self._parser)
            self._COLLADA_SCHEMA_1_4_1_INSTANCE = lxml.etree.XMLSchema(
                    self.COLLADA_SCHEMA_1_4_1_DOC)
        return self._COLLADA_SCHEMA_1_4_1_INSTANCE

    COLLADA_SCHEMA_1_4_1_INSTANCE = property(_getColladaSchemaInstance)
    """An instance of lxml.XMLSchema that can be used to validate"""

    def validate(self, *args, **kwargs):
        """A wrapper for lxml.XMLSchema.validate"""
        return self.COLLADA_SCHEMA_1_4_1_INSTANCE.validate(*args, **kwargs)

