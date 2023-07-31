<?xml version='1.0' encoding='UTF-8'?>
<Project Type="Project" LVVersion="21008000">
	<Item Name="My Computer" Type="My Computer">
		<Property Name="server.app.propertiesEnabled" Type="Bool">true</Property>
		<Property Name="server.control.propertiesEnabled" Type="Bool">true</Property>
		<Property Name="server.tcp.enabled" Type="Bool">false</Property>
		<Property Name="server.tcp.port" Type="Int">0</Property>
		<Property Name="server.tcp.serviceName" Type="Str">My Computer/VI Server</Property>
		<Property Name="server.tcp.serviceName.default" Type="Str">My Computer/VI Server</Property>
		<Property Name="server.vi.callsEnabled" Type="Bool">true</Property>
		<Property Name="server.vi.propertiesEnabled" Type="Bool">true</Property>
		<Property Name="specify.custom.address" Type="Bool">false</Property>
		<Item Name="Main_GEA3.vi" Type="VI" URL="../Main_GEA3.vi"/>
		<Item Name="Dependencies" Type="Dependencies">
			<Item Name="vi.lib" Type="Folder">
				<Item Name="Application Directory.vi" Type="VI" URL="/&lt;vilib&gt;/Utility/file.llb/Application Directory.vi"/>
				<Item Name="BuildHelpPath.vi" Type="VI" URL="/&lt;vilib&gt;/Utility/error.llb/BuildHelpPath.vi"/>
				<Item Name="Check Special Tags.vi" Type="VI" URL="/&lt;vilib&gt;/Utility/error.llb/Check Special Tags.vi"/>
				<Item Name="Clear Errors.vi" Type="VI" URL="/&lt;vilib&gt;/Utility/error.llb/Clear Errors.vi"/>
				<Item Name="Convert property node font to graphics font.vi" Type="VI" URL="/&lt;vilib&gt;/Utility/error.llb/Convert property node font to graphics font.vi"/>
				<Item Name="Details Display Dialog.vi" Type="VI" URL="/&lt;vilib&gt;/Utility/error.llb/Details Display Dialog.vi"/>
				<Item Name="DialogType.ctl" Type="VI" URL="/&lt;vilib&gt;/Utility/error.llb/DialogType.ctl"/>
				<Item Name="DialogTypeEnum.ctl" Type="VI" URL="/&lt;vilib&gt;/Utility/error.llb/DialogTypeEnum.ctl"/>
				<Item Name="Error Cluster From Error Code.vi" Type="VI" URL="/&lt;vilib&gt;/Utility/error.llb/Error Cluster From Error Code.vi"/>
				<Item Name="Error Code Database.vi" Type="VI" URL="/&lt;vilib&gt;/Utility/error.llb/Error Code Database.vi"/>
				<Item Name="ErrWarn.ctl" Type="VI" URL="/&lt;vilib&gt;/Utility/error.llb/ErrWarn.ctl"/>
				<Item Name="eventvkey.ctl" Type="VI" URL="/&lt;vilib&gt;/event_ctls.llb/eventvkey.ctl"/>
				<Item Name="ex_CorrectErrorChain.vi" Type="VI" URL="/&lt;vilib&gt;/express/express shared/ex_CorrectErrorChain.vi"/>
				<Item Name="Find Tag.vi" Type="VI" URL="/&lt;vilib&gt;/Utility/error.llb/Find Tag.vi"/>
				<Item Name="Format Message String.vi" Type="VI" URL="/&lt;vilib&gt;/Utility/error.llb/Format Message String.vi"/>
				<Item Name="General Error Handler Core CORE.vi" Type="VI" URL="/&lt;vilib&gt;/Utility/error.llb/General Error Handler Core CORE.vi"/>
				<Item Name="General Error Handler.vi" Type="VI" URL="/&lt;vilib&gt;/Utility/error.llb/General Error Handler.vi"/>
				<Item Name="Get String Text Bounds.vi" Type="VI" URL="/&lt;vilib&gt;/Utility/error.llb/Get String Text Bounds.vi"/>
				<Item Name="Get Text Rect.vi" Type="VI" URL="/&lt;vilib&gt;/picture/picture.llb/Get Text Rect.vi"/>
				<Item Name="GetHelpDir.vi" Type="VI" URL="/&lt;vilib&gt;/Utility/error.llb/GetHelpDir.vi"/>
				<Item Name="GetRTHostConnectedProp.vi" Type="VI" URL="/&lt;vilib&gt;/Utility/error.llb/GetRTHostConnectedProp.vi"/>
				<Item Name="JDP Utility.lvlib" Type="Library" URL="/&lt;vilib&gt;/JDP Science/JDP Science Common Utilities/JDP Utility.lvlib"/>
				<Item Name="JSONtext.lvlib" Type="Library" URL="/&lt;vilib&gt;/JDP Science/JSONtext/JSONtext.lvlib"/>
				<Item Name="Longest Line Length in Pixels.vi" Type="VI" URL="/&lt;vilib&gt;/Utility/error.llb/Longest Line Length in Pixels.vi"/>
				<Item Name="LVBoundsTypeDef.ctl" Type="VI" URL="/&lt;vilib&gt;/Utility/miscctls.llb/LVBoundsTypeDef.ctl"/>
				<Item Name="LVRectTypeDef.ctl" Type="VI" URL="/&lt;vilib&gt;/Utility/miscctls.llb/LVRectTypeDef.ctl"/>
				<Item Name="NI_FileType.lvlib" Type="Library" URL="/&lt;vilib&gt;/Utility/lvfile.llb/NI_FileType.lvlib"/>
				<Item Name="Not Found Dialog.vi" Type="VI" URL="/&lt;vilib&gt;/Utility/error.llb/Not Found Dialog.vi"/>
				<Item Name="Search and Replace Pattern.vi" Type="VI" URL="/&lt;vilib&gt;/Utility/error.llb/Search and Replace Pattern.vi"/>
				<Item Name="Set Bold Text.vi" Type="VI" URL="/&lt;vilib&gt;/Utility/error.llb/Set Bold Text.vi"/>
				<Item Name="Set String Value.vi" Type="VI" URL="/&lt;vilib&gt;/Utility/error.llb/Set String Value.vi"/>
				<Item Name="Simple Error Handler.vi" Type="VI" URL="/&lt;vilib&gt;/Utility/error.llb/Simple Error Handler.vi"/>
				<Item Name="Space Constant.vi" Type="VI" URL="/&lt;vilib&gt;/dlg_ctls.llb/Space Constant.vi"/>
				<Item Name="subFile Dialog.vi" Type="VI" URL="/&lt;vilib&gt;/express/express input/FileDialogBlock.llb/subFile Dialog.vi"/>
				<Item Name="TagReturnType.ctl" Type="VI" URL="/&lt;vilib&gt;/Utility/error.llb/TagReturnType.ctl"/>
				<Item Name="Three Button Dialog CORE.vi" Type="VI" URL="/&lt;vilib&gt;/Utility/error.llb/Three Button Dialog CORE.vi"/>
				<Item Name="Three Button Dialog.vi" Type="VI" URL="/&lt;vilib&gt;/Utility/error.llb/Three Button Dialog.vi"/>
				<Item Name="Trim Whitespace.vi" Type="VI" URL="/&lt;vilib&gt;/Utility/error.llb/Trim Whitespace.vi"/>
				<Item Name="whitespace.ctl" Type="VI" URL="/&lt;vilib&gt;/Utility/error.llb/whitespace.ctl"/>
			</Item>
			<Item Name="Add_version_to_ERD.vi" Type="VI" URL="../SubVIs/Add_version_to_ERD.vi"/>
			<Item Name="Boatloader_Msg_Entry_Exit.vi" Type="VI" URL="../SubVIs/Boatloader_Msg_Entry_Exit.vi"/>
			<Item Name="Build_Header_Python.vi" Type="VI" URL="../SubVIs/Build_Header_Python.vi"/>
			<Item Name="Build_Header_String_Array.vi" Type="VI" URL="../SubVIs/Build_Header_String_Array.vi"/>
			<Item Name="Command(ERD Loop Control).ctl" Type="VI" URL="../Controles/Command(ERD Loop Control).ctl"/>
			<Item Name="Contro_ERD_Loop.vi" Type="VI" URL="../SubVIs/Contro_ERD_Loop.vi"/>
			<Item Name="Convert_ERDS_GEA.vi" Type="VI" URL="../SubVIs/Convert_ERDS_GEA.vi"/>
			<Item Name="Convert_ERDS_GEA_Version.vi" Type="VI" URL="../SubVIs/Convert_ERDS_GEA_Version.vi"/>
			<Item Name="ERD_Data_Boundled.ctl" Type="VI" URL="../Controles/ERD_Data_Boundled.ctl"/>
			<Item Name="ERD_Data_Frame.vi" Type="VI" URL="../SubVIs/ERD_Data_Frame.vi"/>
			<Item Name="ERD_List.ctl" Type="VI" URL="../Controles/ERD_List.ctl"/>
			<Item Name="ERD_Read_Builder.vi" Type="VI" URL="../SubVIs/ERD_Read_Builder.vi"/>
			<Item Name="Get_User_Filename_and_Path.vi" Type="VI" URL="../SubVIs/Get_User_Filename_and_Path.vi"/>
			<Item Name="GetCurrentDateTimeString.vi" Type="VI" URL="../SubVIs/GetCurrentDateTimeString.vi"/>
			<Item Name="Json_Data_Path_Python.vi" Type="VI" URL="../JSON/Json_Data_Path_Python.vi"/>
			<Item Name="Main_Machine_State.ctl" Type="VI" URL="../Controles/Main_Machine_State.ctl"/>
			<Item Name="Multiple_Read_ERD.ctl" Type="VI" URL="../Controles/Multiple_Read_ERD.ctl"/>
			<Item Name="Open_Create_CSV_File.vi" Type="VI" URL="../SubVIs/Open_Create_CSV_File.vi"/>
			<Item Name="Read_ERD.ctl" Type="VI" URL="../Controles/Read_ERD.ctl"/>
			<Item Name="Read_GEA3.vi" Type="VI" URL="../SubVIs/Read_GEA3.vi"/>
			<Item Name="Read_Multiple_ERD.vi" Type="VI" URL="../SubVIs/Read_Multiple_ERD.vi"/>
			<Item Name="Search_ERD_JSON.vi" Type="VI" URL="../JSON/Search_ERD_JSON.vi"/>
			<Item Name="Search_From_Json.vi" Type="VI" URL="../JSON/Search_From_Json.vi"/>
			<Item Name="Send_Message.ctl" Type="VI" URL="../Controles/Send_Message.ctl"/>
			<Item Name="Send_Message.vi" Type="VI" URL="../SubVIs/Send_Message.vi"/>
			<Item Name="Separate_Bits.vi" Type="VI" URL="../JSON/Separate_Bits.vi"/>
			<Item Name="Set_Board.vi" Type="VI" URL="../SubVIs/Set_Board.vi"/>
			<Item Name="String_Remove_All_Spaces.vi" Type="VI" URL="../SubVIs/String_Remove_All_Spaces.vi"/>
			<Item Name="Time_to_String_Array.vi" Type="VI" URL="../SubVIs/Time_to_String_Array.vi"/>
			<Item Name="UI_Loop_Error_Queue_Setup.vi" Type="VI" URL="../SubVIs/UI_Loop_Error_Queue_Setup.vi"/>
			<Item Name="Value_JSON.vi" Type="VI" URL="../JSON/Value_JSON.vi"/>
			<Item Name="Version_Conversion_Data.vi" Type="VI" URL="../SubVIs/Version_Conversion_Data.vi"/>
			<Item Name="Write _CSV_File_Python.vi" Type="VI" URL="../SubVIs/Write _CSV_File_Python.vi"/>
			<Item Name="Write_ERD.ctl" Type="VI" URL="../Controles/Write_ERD.ctl"/>
			<Item Name="Write_GEA3.vi" Type="VI" URL="../SubVIs/Write_GEA3.vi"/>
			<Item Name="Write_Multiple_ERD.ctl" Type="VI" URL="../Controles/Write_Multiple_ERD.ctl"/>
			<Item Name="Write_Multiple_ERD.vi" Type="VI" URL="../SubVIs/Write_Multiple_ERD.vi"/>
		</Item>
		<Item Name="Build Specifications" Type="Build"/>
	</Item>
</Project>
