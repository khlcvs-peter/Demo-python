import socket
from zeep import Client

# WSDL 服務 URL
wsdl_url = "http://www.w3.org/2001/XMLSchema"

# 建立 SOAP 客戶端
client = Client(wsdl_url)

# 呼叫 GetBasTeacher 方法，傳入 IDKey
response = client.service.GetBasTeacher(IDKey="EC0FC7EF-3EE3-4E0D-ADB6-1FFA8C526AE5")

print("老師資料：", response)


## cu 連線
<wsdl:definitions xmlns:s="http://www.w3.org/2001/XMLSchema" xmlns:soap12="http://schemas.xmlsoap.org/wsdl/soap12/" xmlns:http="http://schemas.xmlsoap.org/wsdl/http/" xmlns:mime="http://schemas.xmlsoap.org/wsdl/mime/" xmlns:tns="http://tempuri.org/" xmlns:soap="http://schemas.xmlsoap.org/wsdl/soap/" xmlns:tm="http://microsoft.com/wsdl/mime/textMatching/" xmlns:soapenc="http://schemas.xmlsoap.org/soap/encoding/" xmlns:wsdl="http://schemas.xmlsoap.org/wsdl/" targetNamespace="http://tempuri.org/">
<wsdl:types>
<s:schema elementFormDefault="qualified" targetNamespace="http://tempuri.org/">
<s:element name="GetBasStu">
<s:complexType>
<s:sequence>
<s:element minOccurs="0" maxOccurs="1" name="IDKey" type="s:string"/>
</s:sequence>
</s:complexType>
</s:element>
<s:element name="GetBasStuResponse">
<s:complexType>
<s:sequence>
<s:element minOccurs="0" maxOccurs="1" name="GetBasStuResult">
<s:complexType>
<s:sequence>
<s:element ref="s:schema"/>
<s:any/>
</s:sequence>
</s:complexType>
</s:element>
<s:element minOccurs="0" maxOccurs="1" name="IDKey" type="s:string"/>
</s:sequence>
</s:complexType>
</s:element>
<s:element name="GetBasStuByStuCode">
<s:complexType>
<s:sequence>
<s:element minOccurs="0" maxOccurs="1" name="IDKey" type="s:string"/>
<s:element minOccurs="0" maxOccurs="1" name="Stucode" type="s:string"/>
</s:sequence>
</s:complexType>
</s:element>
<s:element name="GetBasStuByStuCodeResponse">
<s:complexType>
<s:sequence>
<s:element minOccurs="0" maxOccurs="1" name="GetBasStuByStuCodeResult">
<s:complexType>
<s:sequence>
<s:element ref="s:schema"/>
<s:any/>
</s:sequence>
</s:complexType>
</s:element>
<s:element minOccurs="0" maxOccurs="1" name="IDKey" type="s:string"/>
</s:sequence>
</s:complexType>
</s:element>
<s:element name="GetDiffData">
<s:complexType>
<s:sequence>
<s:element minOccurs="0" maxOccurs="1" name="IDKey" type="s:string"/>
<s:element minOccurs="0" maxOccurs="1" name="tdate" type="s:string"/>
</s:sequence>
</s:complexType>
</s:element>
<s:element name="GetDiffDataResponse">
<s:complexType>
<s:sequence>
<s:element minOccurs="0" maxOccurs="1" name="GetDiffDataResult">
<s:complexType>
<s:sequence>
<s:element ref="s:schema"/>
<s:any/>
</s:sequence>
</s:complexType>
</s:element>
<s:element minOccurs="0" maxOccurs="1" name="IDKey" type="s:string"/>
</s:sequence>
</s:complexType>
</s:element>
<s:element name="GetBasTeacher">
<s:complexType>
<s:sequence>
<s:element minOccurs="0" maxOccurs="1" name="IDKey" type="s:string"/>
</s:sequence>
</s:complexType>
</s:element>
<s:element name="GetBasTeacherResponse">
<s:complexType>
<s:sequence>
<s:element minOccurs="0" maxOccurs="1" name="GetBasTeacherResult">
<s:complexType>
<s:sequence>
<s:element ref="s:schema"/>
<s:any/>
</s:sequence>
</s:complexType>
</s:element>
<s:element minOccurs="0" maxOccurs="1" name="IDKey" type="s:string"/>
</s:sequence>
</s:complexType>
</s:element>
<s:element name="GetBasTeacherByTeacherCode">
<s:complexType>
<s:sequence>
<s:element minOccurs="0" maxOccurs="1" name="IDKey" type="s:string"/>
<s:element minOccurs="0" maxOccurs="1" name="TeacherCode" type="s:string"/>
</s:sequence>
</s:complexType>
</s:element>
<s:element name="GetBasTeacherByTeacherCodeResponse">
<s:complexType>
<s:sequence>
<s:element minOccurs="0" maxOccurs="1" name="GetBasTeacherByTeacherCodeResult">
<s:complexType>
<s:sequence>
<s:element ref="s:schema"/>
<s:any/>
</s:sequence>
</s:complexType>
</s:element>
<s:element minOccurs="0" maxOccurs="1" name="IDKey" type="s:string"/>
</s:sequence>
</s:complexType>
</s:element>
<s:element name="GetCourse">
<s:complexType>
<s:sequence>
<s:element minOccurs="0" maxOccurs="1" name="IDKey" type="s:string"/>
</s:sequence>
</s:complexType>
</s:element>
<s:element name="GetCourseResponse">
<s:complexType>
<s:sequence>
<s:element minOccurs="0" maxOccurs="1" name="GetCourseResult">
<s:complexType>
<s:sequence>
<s:element ref="s:schema"/>
<s:any/>
</s:sequence>
</s:complexType>
</s:element>
<s:element minOccurs="0" maxOccurs="1" name="IDKey" type="s:string"/>
</s:sequence>
</s:complexType>
</s:element>
<s:element name="GetCombinedCourse">
<s:complexType>
<s:sequence>
<s:element minOccurs="0" maxOccurs="1" name="IDKey" type="s:string"/>
</s:sequence>
</s:complexType>
</s:element>
<s:element name="GetCombinedCourseResponse">
<s:complexType>
<s:sequence>
<s:element minOccurs="0" maxOccurs="1" name="GetCombinedCourseResult">
<s:complexType>
<s:sequence>
<s:element ref="s:schema"/>
<s:any/>
</s:sequence>
</s:complexType>
</s:element>
<s:element minOccurs="0" maxOccurs="1" name="IDKey" type="s:string"/>
</s:sequence>
</s:complexType>
</s:element>
<s:element name="GetSummerCombinedCourse">
<s:complexType>
<s:sequence>
<s:element minOccurs="0" maxOccurs="1" name="IDKey" type="s:string"/>
</s:sequence>
</s:complexType>
</s:element>
<s:element name="GetSummerCombinedCourseResponse">
<s:complexType>
<s:sequence>
<s:element minOccurs="0" maxOccurs="1" name="GetSummerCombinedCourseResult">
<s:complexType>
<s:sequence>
<s:element ref="s:schema"/>
<s:any/>
</s:sequence>
</s:complexType>
</s:element>
<s:element minOccurs="0" maxOccurs="1" name="IDKey" type="s:string"/>
</s:sequence>
</s:complexType>
</s:element>
<s:element name="GetDiffCourse">
<s:complexType>
<s:sequence>
<s:element minOccurs="0" maxOccurs="1" name="IDKey" type="s:string"/>
<s:element minOccurs="0" maxOccurs="1" name="tdate" type="s:string"/>
</s:sequence>
</s:complexType>
</s:element>
<s:element name="GetDiffCourseResponse">
<s:complexType>
<s:sequence>
<s:element minOccurs="0" maxOccurs="1" name="GetDiffCourseResult">
<s:complexType>
<s:sequence>
<s:element ref="s:schema"/>
<s:any/>
</s:sequence>
</s:complexType>
</s:element>
<s:element minOccurs="0" maxOccurs="1" name="IDKey" type="s:string"/>
</s:sequence>
</s:complexType>
</s:element>
<s:element name="MutliTeachersCourse">
<s:complexType>
<s:sequence>
<s:element minOccurs="0" maxOccurs="1" name="IDKey" type="s:string"/>
</s:sequence>
</s:complexType>
</s:element>
<s:element name="MutliTeachersCourseResponse">
<s:complexType>
<s:sequence>
<s:element minOccurs="0" maxOccurs="1" name="MutliTeachersCourseResult">
<s:complexType>
<s:sequence>
<s:element ref="s:schema"/>
<s:any/>
</s:sequence>
</s:complexType>
</s:element>
<s:element minOccurs="0" maxOccurs="1" name="IDKey" type="s:string"/>
</s:sequence>
</s:complexType>
</s:element>
<s:element name="MutliTeachersSummerCourse">
<s:complexType>
<s:sequence>
<s:element minOccurs="0" maxOccurs="1" name="IDKey" type="s:string"/>
</s:sequence>
</s:complexType>
</s:element>
<s:element name="MutliTeachersSummerCourseResponse">
<s:complexType>
<s:sequence>
<s:element minOccurs="0" maxOccurs="1" name="MutliTeachersSummerCourseResult">
<s:complexType>
<s:sequence>
<s:element ref="s:schema"/>
<s:any/>
</s:sequence>
</s:complexType>
</s:element>
<s:element minOccurs="0" maxOccurs="1" name="IDKey" type="s:string"/>
</s:sequence>
</s:complexType>
</s:element>
<s:element name="GetStuSelCourse">
<s:complexType>
<s:sequence>
<s:element minOccurs="0" maxOccurs="1" name="IDKey" type="s:string"/>
</s:sequence>
</s:complexType>
</s:element>
<s:element name="GetStuSelCourseResponse">
<s:complexType>
<s:sequence>
<s:element minOccurs="0" maxOccurs="1" name="GetStuSelCourseResult">
<s:complexType>
<s:sequence>
<s:element ref="s:schema"/>
<s:any/>
</s:sequence>
</s:complexType>
</s:element>
<s:element minOccurs="0" maxOccurs="1" name="IDKey" type="s:string"/>
</s:sequence>
</s:complexType>
</s:element>
<s:element name="GetNonElearningCourse">
<s:complexType>
<s:sequence>
<s:element minOccurs="0" maxOccurs="1" name="IDKey" type="s:string"/>
<s:element minOccurs="0" maxOccurs="1" name="CourseCode" type="s:string"/>
</s:sequence>
</s:complexType>
</s:element>
<s:element name="GetNonElearningCourseResponse">
<s:complexType>
<s:sequence>
<s:element minOccurs="0" maxOccurs="1" name="GetNonElearningCourseResult">
<s:complexType>
<s:sequence>
<s:element ref="s:schema"/>
<s:any/>
</s:sequence>
</s:complexType>
</s:element>
<s:element minOccurs="0" maxOccurs="1" name="IDKey" type="s:string"/>
</s:sequence>
</s:complexType>
</s:element>
<s:element name="GetStuNonElearningSelCourse">
<s:complexType>
<s:sequence>
<s:element minOccurs="0" maxOccurs="1" name="IDKey" type="s:string"/>
<s:element minOccurs="0" maxOccurs="1" name="CCODE" type="s:string"/>
</s:sequence>
</s:complexType>
</s:element>
<s:element name="GetStuNonElearningSelCourseResponse">
<s:complexType>
<s:sequence>
<s:element minOccurs="0" maxOccurs="1" name="GetStuNonElearningSelCourseResult">
<s:complexType>
<s:sequence>
<s:element ref="s:schema"/>
<s:any/>
</s:sequence>
</s:complexType>
</s:element>
<s:element minOccurs="0" maxOccurs="1" name="IDKey" type="s:string"/>
</s:sequence>
</s:complexType>
</s:element>
<s:element name="GetSummerCourse">
<s:complexType>
<s:sequence>
<s:element minOccurs="0" maxOccurs="1" name="IDKey" type="s:string"/>
</s:sequence>
</s:complexType>
</s:element>
<s:element name="GetSummerCourseResponse">
<s:complexType>
<s:sequence>
<s:element minOccurs="0" maxOccurs="1" name="GetSummerCourseResult">
<s:complexType>
<s:sequence>
<s:element ref="s:schema"/>
<s:any/>
</s:sequence>
</s:complexType>
</s:element>
<s:element minOccurs="0" maxOccurs="1" name="IDKey" type="s:string"/>
</s:sequence>
</s:complexType>
</s:element>
<s:element name="GetStuSummerSelCourse">
<s:complexType>
<s:sequence>
<s:element minOccurs="0" maxOccurs="1" name="IDKey" type="s:string"/>
</s:sequence>
</s:complexType>
</s:element>
<s:element name="GetStuSummerSelCourseResponse">
<s:complexType>
<s:sequence>
<s:element minOccurs="0" maxOccurs="1" name="GetStuSummerSelCourseResult">
<s:complexType>
<s:sequence>
<s:element ref="s:schema"/>
<s:any/>
</s:sequence>
</s:complexType>
</s:element>
<s:element minOccurs="0" maxOccurs="1" name="IDKey" type="s:string"/>
</s:sequence>
</s:complexType>
</s:element>
<s:element name="GetStuForCourseCount">
<s:complexType>
<s:sequence>
<s:element minOccurs="0" maxOccurs="1" name="IDKey" type="s:string"/>
</s:sequence>
</s:complexType>
</s:element>
<s:element name="GetStuForCourseCountResponse">
<s:complexType>
<s:sequence>
<s:element minOccurs="0" maxOccurs="1" name="GetStuForCourseCountResult">
<s:complexType>
<s:sequence>
<s:element ref="s:schema"/>
<s:any/>
</s:sequence>
</s:complexType>
</s:element>
<s:element minOccurs="0" maxOccurs="1" name="IDKey" type="s:string"/>
</s:sequence>
</s:complexType>
</s:element>
<s:element name="GetStuSelCourseByEnrollStage">
<s:complexType>
<s:sequence>
<s:element minOccurs="0" maxOccurs="1" name="IDKey" type="s:string"/>
<s:element minOccurs="0" maxOccurs="1" name="iSelectType" type="s:string"/>
<s:element minOccurs="0" maxOccurs="1" name="iKind" type="s:string"/>
</s:sequence>
</s:complexType>
</s:element>
<s:element name="GetStuSelCourseByEnrollStageResponse">
<s:complexType>
<s:sequence>
<s:element minOccurs="0" maxOccurs="1" name="GetStuSelCourseByEnrollStageResult">
<s:complexType>
<s:sequence>
<s:element ref="s:schema"/>
<s:any/>
</s:sequence>
</s:complexType>
</s:element>
<s:element minOccurs="0" maxOccurs="1" name="IDKey" type="s:string"/>
</s:sequence>
</s:complexType>
</s:element>
<s:element name="GetDiffStuSelCourse">
<s:complexType>
<s:sequence>
<s:element minOccurs="0" maxOccurs="1" name="IDKey" type="s:string"/>
<s:element minOccurs="0" maxOccurs="1" name="tDate" type="s:string"/>
</s:sequence>
</s:complexType>
</s:element>
<s:element name="GetDiffStuSelCourseResponse">
<s:complexType>
<s:sequence>
<s:element minOccurs="0" maxOccurs="1" name="GetDiffStuSelCourseResult">
<s:complexType>
<s:sequence>
<s:element ref="s:schema"/>
<s:any/>
</s:sequence>
</s:complexType>
</s:element>
<s:element minOccurs="0" maxOccurs="1" name="IDKey" type="s:string"/>
</s:sequence>
</s:complexType>
</s:element>
<s:element name="GetStuSelCourseByStuCode">
<s:complexType>
<s:sequence>
<s:element minOccurs="0" maxOccurs="1" name="IDKey" type="s:string"/>
<s:element minOccurs="0" maxOccurs="1" name="StuCode" type="s:string"/>
</s:sequence>
</s:complexType>
</s:element>
<s:element name="GetStuSelCourseByStuCodeResponse">
<s:complexType>
<s:sequence>
<s:element minOccurs="0" maxOccurs="1" name="GetStuSelCourseByStuCodeResult">
<s:complexType>
<s:sequence>
<s:element ref="s:schema"/>
<s:any/>
</s:sequence>
</s:complexType>
</s:element>
<s:element minOccurs="0" maxOccurs="1" name="IDKey" type="s:string"/>
</s:sequence>
</s:complexType>
</s:element>
<s:element name="GetStuSelCourseByCourse">
<s:complexType>
<s:sequence>
<s:element minOccurs="0" maxOccurs="1" name="IDKey" type="s:string"/>
<s:element minOccurs="0" maxOccurs="1" name="Ccode" type="s:string"/>
</s:sequence>
</s:complexType>
</s:element>
<s:element name="GetStuSelCourseByCourseResponse">
<s:complexType>
<s:sequence>
<s:element minOccurs="0" maxOccurs="1" name="GetStuSelCourseByCourseResult">
<s:complexType>
<s:sequence>
<s:element ref="s:schema"/>
<s:any/>
</s:sequence>
</s:complexType>
</s:element>
<s:element minOccurs="0" maxOccurs="1" name="IDKey" type="s:string"/>
</s:sequence>
</s:complexType>
</s:element>
<s:element name="GetSection">
<s:complexType>
<s:sequence>
<s:element minOccurs="0" maxOccurs="1" name="IDKey" type="s:string"/>
</s:sequence>
</s:complexType>
</s:element>
<s:element name="GetSectionResponse">
<s:complexType>
<s:sequence>
<s:element minOccurs="0" maxOccurs="1" name="GetSectionResult">
<s:complexType>
<s:sequence>
<s:element ref="s:schema"/>
<s:any/>
</s:sequence>
</s:complexType>
</s:element>
<s:element minOccurs="0" maxOccurs="1" name="IDKey" type="s:string"/>
</s:sequence>
</s:complexType>
</s:element>
<s:element name="GetEnrollStage">
<s:complexType>
<s:sequence>
<s:element minOccurs="0" maxOccurs="1" name="IDKey" type="s:string"/>
</s:sequence>
</s:complexType>
</s:element>
<s:element name="GetEnrollStageResponse">
<s:complexType>
<s:sequence>
<s:element minOccurs="0" maxOccurs="1" name="GetEnrollStageResult">
<s:complexType>
<s:sequence>
<s:element ref="s:schema"/>
<s:any/>
</s:sequence>
</s:complexType>
</s:element>
<s:element minOccurs="0" maxOccurs="1" name="IDKey" type="s:string"/>
</s:sequence>
</s:complexType>
</s:element>
<s:element name="LdapAuthForAll">
<s:complexType>
<s:sequence>
<s:element minOccurs="0" maxOccurs="1" name="IDKey" type="s:string"/>
<s:element minOccurs="0" maxOccurs="1" name="account" type="s:string"/>
<s:element minOccurs="0" maxOccurs="1" name="pwd" type="s:string"/>
</s:sequence>
</s:complexType>
</s:element>
<s:element name="LdapAuthForAllResponse">
<s:complexType>
<s:sequence>
<s:element minOccurs="0" maxOccurs="1" name="LdapAuthForAllResult" type="s:string"/>
<s:element minOccurs="0" maxOccurs="1" name="IDKey" type="s:string"/>
</s:sequence>
</s:complexType>
</s:element>
</s:schema>
</wsdl:types>
<wsdl:message name="GetBasStuSoapIn">
<wsdl:part name="parameters" element="tns:GetBasStu"/>
</wsdl:message>
<wsdl:message name="GetBasStuSoapOut">
<wsdl:part name="parameters" element="tns:GetBasStuResponse"/>
</wsdl:message>
<wsdl:message name="GetBasStuByStuCodeSoapIn">
<wsdl:part name="parameters" element="tns:GetBasStuByStuCode"/>
</wsdl:message>
<wsdl:message name="GetBasStuByStuCodeSoapOut">
<wsdl:part name="parameters" element="tns:GetBasStuByStuCodeResponse"/>
</wsdl:message>
<wsdl:message name="GetDiffDataSoapIn">
<wsdl:part name="parameters" element="tns:GetDiffData"/>
</wsdl:message>
<wsdl:message name="GetDiffDataSoapOut">
<wsdl:part name="parameters" element="tns:GetDiffDataResponse"/>
</wsdl:message>
<wsdl:message name="GetBasTeacherSoapIn">
<wsdl:part name="parameters" element="tns:GetBasTeacher"/>
</wsdl:message>
<wsdl:message name="GetBasTeacherSoapOut">
<wsdl:part name="parameters" element="tns:GetBasTeacherResponse"/>
</wsdl:message>
<wsdl:message name="GetBasTeacherByTeacherCodeSoapIn">
<wsdl:part name="parameters" element="tns:GetBasTeacherByTeacherCode"/>
</wsdl:message>
<wsdl:message name="GetBasTeacherByTeacherCodeSoapOut">
<wsdl:part name="parameters" element="tns:GetBasTeacherByTeacherCodeResponse"/>
</wsdl:message>
<wsdl:message name="GetCourseSoapIn">
<wsdl:part name="parameters" element="tns:GetCourse"/>
</wsdl:message>
<wsdl:message name="GetCourseSoapOut">
<wsdl:part name="parameters" element="tns:GetCourseResponse"/>
</wsdl:message>
<wsdl:message name="GetCombinedCourseSoapIn">
<wsdl:part name="parameters" element="tns:GetCombinedCourse"/>
</wsdl:message>
<wsdl:message name="GetCombinedCourseSoapOut">
<wsdl:part name="parameters" element="tns:GetCombinedCourseResponse"/>
</wsdl:message>
<wsdl:message name="GetSummerCombinedCourseSoapIn">
<wsdl:part name="parameters" element="tns:GetSummerCombinedCourse"/>
</wsdl:message>
<wsdl:message name="GetSummerCombinedCourseSoapOut">
<wsdl:part name="parameters" element="tns:GetSummerCombinedCourseResponse"/>
</wsdl:message>
<wsdl:message name="GetDiffCourseSoapIn">
<wsdl:part name="parameters" element="tns:GetDiffCourse"/>
</wsdl:message>
<wsdl:message name="GetDiffCourseSoapOut">
<wsdl:part name="parameters" element="tns:GetDiffCourseResponse"/>
</wsdl:message>
<wsdl:message name="MutliTeachersCourseSoapIn">
<wsdl:part name="parameters" element="tns:MutliTeachersCourse"/>
</wsdl:message>
<wsdl:message name="MutliTeachersCourseSoapOut">
<wsdl:part name="parameters" element="tns:MutliTeachersCourseResponse"/>
</wsdl:message>
<wsdl:message name="MutliTeachersSummerCourseSoapIn">
<wsdl:part name="parameters" element="tns:MutliTeachersSummerCourse"/>
</wsdl:message>
<wsdl:message name="MutliTeachersSummerCourseSoapOut">
<wsdl:part name="parameters" element="tns:MutliTeachersSummerCourseResponse"/>
</wsdl:message>
<wsdl:message name="GetStuSelCourseSoapIn">
<wsdl:part name="parameters" element="tns:GetStuSelCourse"/>
</wsdl:message>
<wsdl:message name="GetStuSelCourseSoapOut">
<wsdl:part name="parameters" element="tns:GetStuSelCourseResponse"/>
</wsdl:message>
<wsdl:message name="GetNonElearningCourseSoapIn">
<wsdl:part name="parameters" element="tns:GetNonElearningCourse"/>
</wsdl:message>
<wsdl:message name="GetNonElearningCourseSoapOut">
<wsdl:part name="parameters" element="tns:GetNonElearningCourseResponse"/>
</wsdl:message>
<wsdl:message name="GetStuNonElearningSelCourseSoapIn">
<wsdl:part name="parameters" element="tns:GetStuNonElearningSelCourse"/>
</wsdl:message>
<wsdl:message name="GetStuNonElearningSelCourseSoapOut">
<wsdl:part name="parameters" element="tns:GetStuNonElearningSelCourseResponse"/>
</wsdl:message>
<wsdl:message name="GetSummerCourseSoapIn">
<wsdl:part name="parameters" element="tns:GetSummerCourse"/>
</wsdl:message>
<wsdl:message name="GetSummerCourseSoapOut">
<wsdl:part name="parameters" element="tns:GetSummerCourseResponse"/>
</wsdl:message>
<wsdl:message name="GetStuSummerSelCourseSoapIn">
<wsdl:part name="parameters" element="tns:GetStuSummerSelCourse"/>
</wsdl:message>
<wsdl:message name="GetStuSummerSelCourseSoapOut">
<wsdl:part name="parameters" element="tns:GetStuSummerSelCourseResponse"/>
</wsdl:message>
<wsdl:message name="GetStuForCourseCountSoapIn">
<wsdl:part name="parameters" element="tns:GetStuForCourseCount"/>
</wsdl:message>
<wsdl:message name="GetStuForCourseCountSoapOut">
<wsdl:part name="parameters" element="tns:GetStuForCourseCountResponse"/>
</wsdl:message>
<wsdl:message name="GetStuSelCourseByEnrollStageSoapIn">
<wsdl:part name="parameters" element="tns:GetStuSelCourseByEnrollStage"/>
</wsdl:message>
<wsdl:message name="GetStuSelCourseByEnrollStageSoapOut">
<wsdl:part name="parameters" element="tns:GetStuSelCourseByEnrollStageResponse"/>
</wsdl:message>
<wsdl:message name="GetDiffStuSelCourseSoapIn">
<wsdl:part name="parameters" element="tns:GetDiffStuSelCourse"/>
</wsdl:message>
<wsdl:message name="GetDiffStuSelCourseSoapOut">
<wsdl:part name="parameters" element="tns:GetDiffStuSelCourseResponse"/>
</wsdl:message>
<wsdl:message name="GetStuSelCourseByStuCodeSoapIn">
<wsdl:part name="parameters" element="tns:GetStuSelCourseByStuCode"/>
</wsdl:message>
<wsdl:message name="GetStuSelCourseByStuCodeSoapOut">
<wsdl:part name="parameters" element="tns:GetStuSelCourseByStuCodeResponse"/>
</wsdl:message>
<wsdl:message name="GetStuSelCourseByCourseSoapIn">
<wsdl:part name="parameters" element="tns:GetStuSelCourseByCourse"/>
</wsdl:message>
<wsdl:message name="GetStuSelCourseByCourseSoapOut">
<wsdl:part name="parameters" element="tns:GetStuSelCourseByCourseResponse"/>
</wsdl:message>
<wsdl:message name="GetSectionSoapIn">
<wsdl:part name="parameters" element="tns:GetSection"/>
</wsdl:message>
<wsdl:message name="GetSectionSoapOut">
<wsdl:part name="parameters" element="tns:GetSectionResponse"/>
</wsdl:message>
<wsdl:message name="GetEnrollStageSoapIn">
<wsdl:part name="parameters" element="tns:GetEnrollStage"/>
</wsdl:message>
<wsdl:message name="GetEnrollStageSoapOut">
<wsdl:part name="parameters" element="tns:GetEnrollStageResponse"/>
</wsdl:message>
<wsdl:message name="LdapAuthForAllSoapIn">
<wsdl:part name="parameters" element="tns:LdapAuthForAll"/>
</wsdl:message>
<wsdl:message name="LdapAuthForAllSoapOut">
<wsdl:part name="parameters" element="tns:LdapAuthForAllResponse"/>
</wsdl:message>
<wsdl:portType name="WebService1Soap">
<wsdl:operation name="GetBasStu">
<wsdl:input message="tns:GetBasStuSoapIn"/>
<wsdl:output message="tns:GetBasStuSoapOut"/>
</wsdl:operation>
<wsdl:operation name="GetBasStuByStuCode">
<wsdl:input message="tns:GetBasStuByStuCodeSoapIn"/>
<wsdl:output message="tns:GetBasStuByStuCodeSoapOut"/>
</wsdl:operation>
<wsdl:operation name="GetDiffData">
<wsdl:input message="tns:GetDiffDataSoapIn"/>
<wsdl:output message="tns:GetDiffDataSoapOut"/>
</wsdl:operation>
<wsdl:operation name="GetBasTeacher">
<wsdl:input message="tns:GetBasTeacherSoapIn"/>
<wsdl:output message="tns:GetBasTeacherSoapOut"/>
</wsdl:operation>
<wsdl:operation name="GetBasTeacherByTeacherCode">
<wsdl:input message="tns:GetBasTeacherByTeacherCodeSoapIn"/>
<wsdl:output message="tns:GetBasTeacherByTeacherCodeSoapOut"/>
</wsdl:operation>
<wsdl:operation name="GetCourse">
<wsdl:input message="tns:GetCourseSoapIn"/>
<wsdl:output message="tns:GetCourseSoapOut"/>
</wsdl:operation>
<wsdl:operation name="GetCombinedCourse">
<wsdl:input message="tns:GetCombinedCourseSoapIn"/>
<wsdl:output message="tns:GetCombinedCourseSoapOut"/>
</wsdl:operation>
<wsdl:operation name="GetSummerCombinedCourse">
<wsdl:input message="tns:GetSummerCombinedCourseSoapIn"/>
<wsdl:output message="tns:GetSummerCombinedCourseSoapOut"/>
</wsdl:operation>
<wsdl:operation name="GetDiffCourse">
<wsdl:input message="tns:GetDiffCourseSoapIn"/>
<wsdl:output message="tns:GetDiffCourseSoapOut"/>
</wsdl:operation>
<wsdl:operation name="MutliTeachersCourse">
<wsdl:input message="tns:MutliTeachersCourseSoapIn"/>
<wsdl:output message="tns:MutliTeachersCourseSoapOut"/>
</wsdl:operation>
<wsdl:operation name="MutliTeachersSummerCourse">
<wsdl:input message="tns:MutliTeachersSummerCourseSoapIn"/>
<wsdl:output message="tns:MutliTeachersSummerCourseSoapOut"/>
</wsdl:operation>
<wsdl:operation name="GetStuSelCourse">
<wsdl:input message="tns:GetStuSelCourseSoapIn"/>
<wsdl:output message="tns:GetStuSelCourseSoapOut"/>
</wsdl:operation>
<wsdl:operation name="GetNonElearningCourse">
<wsdl:input message="tns:GetNonElearningCourseSoapIn"/>
<wsdl:output message="tns:GetNonElearningCourseSoapOut"/>
</wsdl:operation>
<wsdl:operation name="GetStuNonElearningSelCourse">
<wsdl:input message="tns:GetStuNonElearningSelCourseSoapIn"/>
<wsdl:output message="tns:GetStuNonElearningSelCourseSoapOut"/>
</wsdl:operation>
<wsdl:operation name="GetSummerCourse">
<wsdl:input message="tns:GetSummerCourseSoapIn"/>
<wsdl:output message="tns:GetSummerCourseSoapOut"/>
</wsdl:operation>
<wsdl:operation name="GetStuSummerSelCourse">
<wsdl:input message="tns:GetStuSummerSelCourseSoapIn"/>
<wsdl:output message="tns:GetStuSummerSelCourseSoapOut"/>
</wsdl:operation>
<wsdl:operation name="GetStuForCourseCount">
<wsdl:input message="tns:GetStuForCourseCountSoapIn"/>
<wsdl:output message="tns:GetStuForCourseCountSoapOut"/>
</wsdl:operation>
<wsdl:operation name="GetStuSelCourseByEnrollStage">
<wsdl:input message="tns:GetStuSelCourseByEnrollStageSoapIn"/>
<wsdl:output message="tns:GetStuSelCourseByEnrollStageSoapOut"/>
</wsdl:operation>
<wsdl:operation name="GetDiffStuSelCourse">
<wsdl:input message="tns:GetDiffStuSelCourseSoapIn"/>
<wsdl:output message="tns:GetDiffStuSelCourseSoapOut"/>
</wsdl:operation>
<wsdl:operation name="GetStuSelCourseByStuCode">
<wsdl:input message="tns:GetStuSelCourseByStuCodeSoapIn"/>
<wsdl:output message="tns:GetStuSelCourseByStuCodeSoapOut"/>
</wsdl:operation>
<wsdl:operation name="GetStuSelCourseByCourse">
<wsdl:input message="tns:GetStuSelCourseByCourseSoapIn"/>
<wsdl:output message="tns:GetStuSelCourseByCourseSoapOut"/>
</wsdl:operation>
<wsdl:operation name="GetSection">
<wsdl:input message="tns:GetSectionSoapIn"/>
<wsdl:output message="tns:GetSectionSoapOut"/>
</wsdl:operation>
<wsdl:operation name="GetEnrollStage">
<wsdl:input message="tns:GetEnrollStageSoapIn"/>
<wsdl:output message="tns:GetEnrollStageSoapOut"/>
</wsdl:operation>
<wsdl:operation name="LdapAuthForAll">
<wsdl:input message="tns:LdapAuthForAllSoapIn"/>
<wsdl:output message="tns:LdapAuthForAllSoapOut"/>
</wsdl:operation>
</wsdl:portType>
<wsdl:binding name="WebService1Soap" type="tns:WebService1Soap">
<soap:binding transport="http://schemas.xmlsoap.org/soap/http"/>
<wsdl:operation name="GetBasStu">
<soap:operation soapAction="http://tempuri.org/GetBasStu" style="document"/>
<wsdl:input>
<soap:body use="literal"/>
</wsdl:input>
<wsdl:output>
<soap:body use="literal"/>
</wsdl:output>
</wsdl:operation>
<wsdl:operation name="GetBasStuByStuCode">
<soap:operation soapAction="http://tempuri.org/GetBasStuByStuCode" style="document"/>
<wsdl:input>
<soap:body use="literal"/>
</wsdl:input>
<wsdl:output>
<soap:body use="literal"/>
</wsdl:output>
</wsdl:operation>
<wsdl:operation name="GetDiffData">
<soap:operation soapAction="http://tempuri.org/GetDiffData" style="document"/>
<wsdl:input>
<soap:body use="literal"/>
</wsdl:input>
<wsdl:output>
<soap:body use="literal"/>
</wsdl:output>
</wsdl:operation>
<wsdl:operation name="GetBasTeacher">
<soap:operation soapAction="http://tempuri.org/GetBasTeacher" style="document"/>
<wsdl:input>
<soap:body use="literal"/>
</wsdl:input>
<wsdl:output>
<soap:body use="literal"/>
</wsdl:output>
</wsdl:operation>
<wsdl:operation name="GetBasTeacherByTeacherCode">
<soap:operation soapAction="http://tempuri.org/GetBasTeacherByTeacherCode" style="document"/>
<wsdl:input>
<soap:body use="literal"/>
</wsdl:input>
<wsdl:output>
<soap:body use="literal"/>
</wsdl:output>
</wsdl:operation>
<wsdl:operation name="GetCourse">
<soap:operation soapAction="http://tempuri.org/GetCourse" style="document"/>
<wsdl:input>
<soap:body use="literal"/>
</wsdl:input>
<wsdl:output>
<soap:body use="literal"/>
</wsdl:output>
</wsdl:operation>
<wsdl:operation name="GetCombinedCourse">
<soap:operation soapAction="http://tempuri.org/GetCombinedCourse" style="document"/>
<wsdl:input>
<soap:body use="literal"/>
</wsdl:input>
<wsdl:output>
<soap:body use="literal"/>
</wsdl:output>
</wsdl:operation>
<wsdl:operation name="GetSummerCombinedCourse">
<soap:operation soapAction="http://tempuri.org/GetSummerCombinedCourse" style="document"/>
<wsdl:input>
<soap:body use="literal"/>
</wsdl:input>
<wsdl:output>
<soap:body use="literal"/>
</wsdl:output>
</wsdl:operation>
<wsdl:operation name="GetDiffCourse">
<soap:operation soapAction="http://tempuri.org/GetDiffCourse" style="document"/>
<wsdl:input>
<soap:body use="literal"/>
</wsdl:input>
<wsdl:output>
<soap:body use="literal"/>
</wsdl:output>
</wsdl:operation>
<wsdl:operation name="MutliTeachersCourse">
<soap:operation soapAction="http://tempuri.org/MutliTeachersCourse" style="document"/>
<wsdl:input>
<soap:body use="literal"/>
</wsdl:input>
<wsdl:output>
<soap:body use="literal"/>
</wsdl:output>
</wsdl:operation>
<wsdl:operation name="MutliTeachersSummerCourse">
<soap:operation soapAction="http://tempuri.org/MutliTeachersSummerCourse" style="document"/>
<wsdl:input>
<soap:body use="literal"/>
</wsdl:input>
<wsdl:output>
<soap:body use="literal"/>
</wsdl:output>
</wsdl:operation>
<wsdl:operation name="GetStuSelCourse">
<soap:operation soapAction="http://tempuri.org/GetStuSelCourse" style="document"/>
<wsdl:input>
<soap:body use="literal"/>
</wsdl:input>
<wsdl:output>
<soap:body use="literal"/>
</wsdl:output>
</wsdl:operation>
<wsdl:operation name="GetNonElearningCourse">
<soap:operation soapAction="http://tempuri.org/GetNonElearningCourse" style="document"/>
<wsdl:input>
<soap:body use="literal"/>
</wsdl:input>
<wsdl:output>
<soap:body use="literal"/>
</wsdl:output>
</wsdl:operation>
<wsdl:operation name="GetStuNonElearningSelCourse">
<soap:operation soapAction="http://tempuri.org/GetStuNonElearningSelCourse" style="document"/>
<wsdl:input>
<soap:body use="literal"/>
</wsdl:input>
<wsdl:output>
<soap:body use="literal"/>
</wsdl:output>
</wsdl:operation>
<wsdl:operation name="GetSummerCourse">
<soap:operation soapAction="http://tempuri.org/GetSummerCourse" style="document"/>
<wsdl:input>
<soap:body use="literal"/>
</wsdl:input>
<wsdl:output>
<soap:body use="literal"/>
</wsdl:output>
</wsdl:operation>
<wsdl:operation name="GetStuSummerSelCourse">
<soap:operation soapAction="http://tempuri.org/GetStuSummerSelCourse" style="document"/>
<wsdl:input>
<soap:body use="literal"/>
</wsdl:input>
<wsdl:output>
<soap:body use="literal"/>
</wsdl:output>
</wsdl:operation>
<wsdl:operation name="GetStuForCourseCount">
<soap:operation soapAction="http://tempuri.org/GetStuForCourseCount" style="document"/>
<wsdl:input>
<soap:body use="literal"/>
</wsdl:input>
<wsdl:output>
<soap:body use="literal"/>
</wsdl:output>
</wsdl:operation>
<wsdl:operation name="GetStuSelCourseByEnrollStage">
<soap:operation soapAction="http://tempuri.org/GetStuSelCourseByEnrollStage" style="document"/>
<wsdl:input>
<soap:body use="literal"/>
</wsdl:input>
<wsdl:output>
<soap:body use="literal"/>
</wsdl:output>
</wsdl:operation>
<wsdl:operation name="GetDiffStuSelCourse">
<soap:operation soapAction="http://tempuri.org/GetDiffStuSelCourse" style="document"/>
<wsdl:input>
<soap:body use="literal"/>
</wsdl:input>
<wsdl:output>
<soap:body use="literal"/>
</wsdl:output>
</wsdl:operation>
<wsdl:operation name="GetStuSelCourseByStuCode">
<soap:operation soapAction="http://tempuri.org/GetStuSelCourseByStuCode" style="document"/>
<wsdl:input>
<soap:body use="literal"/>
</wsdl:input>
<wsdl:output>
<soap:body use="literal"/>
</wsdl:output>
</wsdl:operation>
<wsdl:operation name="GetStuSelCourseByCourse">
<soap:operation soapAction="http://tempuri.org/GetStuSelCourseByCourse" style="document"/>
<wsdl:input>
<soap:body use="literal"/>
</wsdl:input>
<wsdl:output>
<soap:body use="literal"/>
</wsdl:output>
</wsdl:operation>
<wsdl:operation name="GetSection">
<soap:operation soapAction="http://tempuri.org/GetSection" style="document"/>
<wsdl:input>
<soap:body use="literal"/>
</wsdl:input>
<wsdl:output>
<soap:body use="literal"/>
</wsdl:output>
</wsdl:operation>
<wsdl:operation name="GetEnrollStage">
<soap:operation soapAction="http://tempuri.org/GetEnrollStage" style="document"/>
<wsdl:input>
<soap:body use="literal"/>
</wsdl:input>
<wsdl:output>
<soap:body use="literal"/>
</wsdl:output>
</wsdl:operation>
<wsdl:operation name="LdapAuthForAll">
<soap:operation soapAction="http://tempuri.org/LdapAuthForAll" style="document"/>
<wsdl:input>
<soap:body use="literal"/>
</wsdl:input>
<wsdl:output>
<soap:body use="literal"/>
</wsdl:output>
</wsdl:operation>
</wsdl:binding>
<wsdl:binding name="WebService1Soap12" type="tns:WebService1Soap">
<soap12:binding transport="http://schemas.xmlsoap.org/soap/http"/>
<wsdl:operation name="GetBasStu">
<soap12:operation soapAction="http://tempuri.org/GetBasStu" style="document"/>
<wsdl:input>
<soap12:body use="literal"/>
</wsdl:input>
<wsdl:output>
<soap12:body use="literal"/>
</wsdl:output>
</wsdl:operation>
<wsdl:operation name="GetBasStuByStuCode">
<soap12:operation soapAction="http://tempuri.org/GetBasStuByStuCode" style="document"/>
<wsdl:input>
<soap12:body use="literal"/>
</wsdl:input>
<wsdl:output>
<soap12:body use="literal"/>
</wsdl:output>
</wsdl:operation>
<wsdl:operation name="GetDiffData">
<soap12:operation soapAction="http://tempuri.org/GetDiffData" style="document"/>
<wsdl:input>
<soap12:body use="literal"/>
</wsdl:input>
<wsdl:output>
<soap12:body use="literal"/>
</wsdl:output>
</wsdl:operation>
<wsdl:operation name="GetBasTeacher">
<soap12:operation soapAction="http://tempuri.org/GetBasTeacher" style="document"/>
<wsdl:input>
<soap12:body use="literal"/>
</wsdl:input>
<wsdl:output>
<soap12:body use="literal"/>
</wsdl:output>
</wsdl:operation>
<wsdl:operation name="GetBasTeacherByTeacherCode">
<soap12:operation soapAction="http://tempuri.org/GetBasTeacherByTeacherCode" style="document"/>
<wsdl:input>
<soap12:body use="literal"/>
</wsdl:input>
<wsdl:output>
<soap12:body use="literal"/>
</wsdl:output>
</wsdl:operation>
<wsdl:operation name="GetCourse">
<soap12:operation soapAction="http://tempuri.org/GetCourse" style="document"/>
<wsdl:input>
<soap12:body use="literal"/>
</wsdl:input>
<wsdl:output>
<soap12:body use="literal"/>
</wsdl:output>
</wsdl:operation>
<wsdl:operation name="GetCombinedCourse">
<soap12:operation soapAction="http://tempuri.org/GetCombinedCourse" style="document"/>
<wsdl:input>
<soap12:body use="literal"/>
</wsdl:input>
<wsdl:output>
<soap12:body use="literal"/>
</wsdl:output>
</wsdl:operation>
<wsdl:operation name="GetSummerCombinedCourse">
<soap12:operation soapAction="http://tempuri.org/GetSummerCombinedCourse" style="document"/>
<wsdl:input>
<soap12:body use="literal"/>
</wsdl:input>
<wsdl:output>
<soap12:body use="literal"/>
</wsdl:output>
</wsdl:operation>
<wsdl:operation name="GetDiffCourse">
<soap12:operation soapAction="http://tempuri.org/GetDiffCourse" style="document"/>
<wsdl:input>
<soap12:body use="literal"/>
</wsdl:input>
<wsdl:output>
<soap12:body use="literal"/>
</wsdl:output>
</wsdl:operation>
<wsdl:operation name="MutliTeachersCourse">
<soap12:operation soapAction="http://tempuri.org/MutliTeachersCourse" style="document"/>
<wsdl:input>
<soap12:body use="literal"/>
</wsdl:input>
<wsdl:output>
<soap12:body use="literal"/>
</wsdl:output>
</wsdl:operation>
<wsdl:operation name="MutliTeachersSummerCourse">
<soap12:operation soapAction="http://tempuri.org/MutliTeachersSummerCourse" style="document"/>
<wsdl:input>
<soap12:body use="literal"/>
</wsdl:input>
<wsdl:output>
<soap12:body use="literal"/>
</wsdl:output>
</wsdl:operation>
<wsdl:operation name="GetStuSelCourse">
<soap12:operation soapAction="http://tempuri.org/GetStuSelCourse" style="document"/>
<wsdl:input>
<soap12:body use="literal"/>
</wsdl:input>
<wsdl:output>
<soap12:body use="literal"/>
</wsdl:output>
</wsdl:operation>
<wsdl:operation name="GetNonElearningCourse">
<soap12:operation soapAction="http://tempuri.org/GetNonElearningCourse" style="document"/>
<wsdl:input>
<soap12:body use="literal"/>
</wsdl:input>
<wsdl:output>
<soap12:body use="literal"/>
</wsdl:output>
</wsdl:operation>
<wsdl:operation name="GetStuNonElearningSelCourse">
<soap12:operation soapAction="http://tempuri.org/GetStuNonElearningSelCourse" style="document"/>
<wsdl:input>
<soap12:body use="literal"/>
</wsdl:input>
<wsdl:output>
<soap12:body use="literal"/>
</wsdl:output>
</wsdl:operation>
<wsdl:operation name="GetSummerCourse">
<soap12:operation soapAction="http://tempuri.org/GetSummerCourse" style="document"/>
<wsdl:input>
<soap12:body use="literal"/>
</wsdl:input>
<wsdl:output>
<soap12:body use="literal"/>
</wsdl:output>
</wsdl:operation>
<wsdl:operation name="GetStuSummerSelCourse">
<soap12:operation soapAction="http://tempuri.org/GetStuSummerSelCourse" style="document"/>
<wsdl:input>
<soap12:body use="literal"/>
</wsdl:input>
<wsdl:output>
<soap12:body use="literal"/>
</wsdl:output>
</wsdl:operation>
<wsdl:operation name="GetStuForCourseCount">
<soap12:operation soapAction="http://tempuri.org/GetStuForCourseCount" style="document"/>
<wsdl:input>
<soap12:body use="literal"/>
</wsdl:input>
<wsdl:output>
<soap12:body use="literal"/>
</wsdl:output>
</wsdl:operation>
<wsdl:operation name="GetStuSelCourseByEnrollStage">
<soap12:operation soapAction="http://tempuri.org/GetStuSelCourseByEnrollStage" style="document"/>
<wsdl:input>
<soap12:body use="literal"/>
</wsdl:input>
<wsdl:output>
<soap12:body use="literal"/>
</wsdl:output>
</wsdl:operation>
<wsdl:operation name="GetDiffStuSelCourse">
<soap12:operation soapAction="http://tempuri.org/GetDiffStuSelCourse" style="document"/>
<wsdl:input>
<soap12:body use="literal"/>
</wsdl:input>
<wsdl:output>
<soap12:body use="literal"/>
</wsdl:output>
</wsdl:operation>
<wsdl:operation name="GetStuSelCourseByStuCode">
<soap12:operation soapAction="http://tempuri.org/GetStuSelCourseByStuCode" style="document"/>
<wsdl:input>
<soap12:body use="literal"/>
</wsdl:input>
<wsdl:output>
<soap12:body use="literal"/>
</wsdl:output>
</wsdl:operation>
<wsdl:operation name="GetStuSelCourseByCourse">
<soap12:operation soapAction="http://tempuri.org/GetStuSelCourseByCourse" style="document"/>
<wsdl:input>
<soap12:body use="literal"/>
</wsdl:input>
<wsdl:output>
<soap12:body use="literal"/>
</wsdl:output>
</wsdl:operation>
<wsdl:operation name="GetSection">
<soap12:operation soapAction="http://tempuri.org/GetSection" style="document"/>
<wsdl:input>
<soap12:body use="literal"/>
</wsdl:input>
<wsdl:output>
<soap12:body use="literal"/>
</wsdl:output>
</wsdl:operation>
<wsdl:operation name="GetEnrollStage">
<soap12:operation soapAction="http://tempuri.org/GetEnrollStage" style="document"/>
<wsdl:input>
<soap12:body use="literal"/>
</wsdl:input>
<wsdl:output>
<soap12:body use="literal"/>
</wsdl:output>
</wsdl:operation>
<wsdl:operation name="LdapAuthForAll">
<soap12:operation soapAction="http://tempuri.org/LdapAuthForAll" style="document"/>
<wsdl:input>
<soap12:body use="literal"/>
</wsdl:input>
<wsdl:output>
<soap12:body use="literal"/>
</wsdl:output>
</wsdl:operation>
</wsdl:binding>
<wsdl:service name="WebService1">
<wsdl:port name="WebService1Soap" binding="tns:WebService1Soap">
<soap:address location="https://mfser.stu.edu.tw/wbsforcuserviceapi/webservice1.asmx"/>
</wsdl:port>
<wsdl:port name="WebService1Soap12" binding="tns:WebService1Soap12">
<soap12:address location="https://mfser.stu.edu.tw/wbsforcuserviceapi/webservice1.asmx"/>
</wsdl:port>
</wsdl:service>
</wsdl:definitions>