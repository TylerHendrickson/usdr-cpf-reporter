from datetime import datetime
from enum import Enum
from typing import Optional

from pydantic import (BaseModel, ConfigDict, Field, condecimal, conint,
                      validator)


class StateAbbreviation(Enum):
    AL = "AL"
    AK = "AK"
    AZ = "AZ"
    AR = "AR"
    CA = "CA"
    CO = "CO"
    CT = "CT"
    DE = "DE"
    FL = "FL"
    GA = "GA"
    HI = "HI"
    ID = "ID"
    IL = "IL"
    IN = "IN"
    IA = "IA"
    KS = "KS"
    KY = "KY"
    LA = "LA"
    ME = "ME"
    MD = "MD"
    MA = "MA"
    MI = "MI"
    MN = "MN"
    MS = "MS"
    MO = "MO"
    MT = "MT"
    NE = "NE"
    NV = "NV"
    NH = "NH"
    NJ = "NJ"
    NM = "NM"
    NY = "NY"
    NC = "NC"
    ND = "ND"
    OH = "OH"
    OK = "OK"
    OR = "OR"
    PA = "PA"
    RI = "RI"
    SC = "SC"
    SD = "SD"
    TN = "TN"
    TX = "TX"
    UT = "UT"
    VT = "VT"
    VA = "VA"
    WA = "WA"
    WV = "WV"
    WI = "WI"
    WY = "WY"


class CapitalAssetOwnershipType(str, Enum):
    PRIVATE = "1. Private"
    STATE_GOVERNMENT = "2. State Government"
    MUNICIPAL_OR_TOWNSHIP_GOVERNMENT = "3. Municipal or Township Government"
    COUNTY_GOVERNMENT = "4. County Government"
    TRIBAL_GOVERNMENT = "5. Tribal Government"
    COOPERATIVE = "6. Co-operative"
    OTHER = "7. Other"


class ProjectStatusType(str, Enum):
    NOT_STARTED = "1. Not Started"
    LESS_THAN_FIFTY_PERCENT_COMPLETE = "2. Less than 50 percent complete"
    MORE_THAN_FIFTY_PERCENT_COMPLETE = "3. More than 50 percent complete"
    COMPLETED = "4. Completed"


class YesNoType(str, Enum):
    YES = "Yes"
    NO = "No"


class TechType(str, Enum):
    FIBER = "1. Fiber"
    COAXIAL_CABLE = "2. Coaxial Cable"
    FIXED_WIRELESS = "3. Fixed Wireless"
    OTHER = "4. Other"


class ProjectInvestmentType(str, Enum):
    NEW_CONSTRUCTION = "1. New Construction"
    RENOVATION = "2. Renovation"


class BaseProjectRow(BaseModel):
    model_config = ConfigDict(coerce_numbers_to_str=True, loc_by_alias=False)

    Project_Name__c: str = Field(
        ..., serialization_alias="Project Name", max_length=100, json_schema_extra={"column":"C"}
    )
    Identification_Number__c: str = Field(
        ..., serialization_alias="Identification Number", max_length=20, json_schema_extra={"column":"D"}
    )
    Project_Description__c: str = Field(
        ..., serialization_alias="Project Description", max_length=3000, json_schema_extra={"column":"E"}
    )
    Capital_Asset_Ownership_Type__c: CapitalAssetOwnershipType = Field(
        ..., serialization_alias="Capital Asset Owenership Type", json_schema_extra={"column":"F"}
    )
    Total_CPF_Funding_for_Project__c: condecimal(max_digits=13, decimal_places=2) = (
        Field(..., serialization_alias="Total CPF Funding for Project", json_schema_extra={"column":"G"})
    )
    Total_from_all_funding_sources__c: condecimal(max_digits=13, decimal_places=2) = (
        Field(..., serialization_alias="Total From all Funding Sources", json_schema_extra={"column":"H"})
    )
    Narrative_Description__c: Optional[str] = Field(
        default=None, serialization_alias="Narrative Description", max_length=3000, json_schema_extra={"column":"I"}
    )
    Current_Period_Obligation__c: condecimal(max_digits=12, decimal_places=2) = Field(
        ..., serialization_alias="Current Period Obligation", json_schema_extra={"column":"J"}
    )
    Current_Period_Expenditure__c: condecimal(max_digits=12, decimal_places=2) = Field(
        ..., serialization_alias="Current Period Expenditure", json_schema_extra={"column":"K"}
    )
    Cumulative_Obligation__c: condecimal(max_digits=12, decimal_places=2) = Field(
        ..., serialization_alias="Cumulative Obligation", json_schema_extra={"column":"L"}
    )
    Cumulative_Expenditure__c: condecimal(max_digits=12, decimal_places=2) = Field(
        ..., serialization_alias="Cumulative Expenditure", json_schema_extra={"column":"M"}
    )
    Cost_Overview__c: str = Field(
        ..., serialization_alias="Cost Overview", max_length=3000, json_schema_extra={"column":"N"}
    )
    Project_Status__c: ProjectStatusType = Field(
        ..., serialization_alias="Project Status", json_schema_extra={"column":"O"}
    )
    Projected_Con_Start_Date__c: Optional[datetime] = Field(
        default=None, serialization_alias="Projected Con. Start Date", json_schema_extra={"column":"P"}
    )
    Projected_Con_Completion__c: Optional[datetime] = Field(
        default=None, serialization_alias="Projected Con. Completion", json_schema_extra={"column":"Q"}
    )
    Projected_Init_of_Operations__c: Optional[datetime] = Field(
        default=None, serialization_alias="Projected Init. of Operations", json_schema_extra={"column":"R"}
    )
    Actual_Con_Start_Date__c: Optional[datetime] = Field(
        default=None, serialization_alias="Actual Con. Start Date", json_schema_extra={"column":"S"}
    )
    Actual_Con_Completion__c: Optional[datetime] = Field(
        default=None, serialization_alias="Actual Con. Completion", json_schema_extra={"column":"T"}
    )
    Operations_initiated__c: Optional[YesNoType] = Field(
        default=None, serialization_alias="Operations Initiated", json_schema_extra={"column":"U"}
    )
    Actual_operations_date__c: Optional[datetime] = Field(
        default=None, serialization_alias="Actual operations date", json_schema_extra={"column":"V"}
    )
    Operations_explanation__c: Optional[str] = Field(
        default=None, serialization_alias="Operations explanation", max_length=3000, json_schema_extra={"column":"W"}
    )
    Other_Federal_Funding__c: YesNoType = Field(
        ..., serialization_alias="Other Federal Funding?", json_schema_extra={"column":"X"}
    )
    Matching_Funds__c: YesNoType = Field(..., serialization_alias="Matching Funds?", json_schema_extra={"column":"Y"})
    Program_Information__c: Optional[str] = Field(
        default=None, serialization_alias="Program Information", max_length=50, json_schema_extra={"column":"Z"}
    )
    Amount_of_Matching_Funds__c: Optional[
        condecimal(max_digits=12, decimal_places=2)
    ] = Field(default=None, serialization_alias="Amount of Matching Funds", json_schema_extra={"column":"AA"})
    Target_Project_Info__c: Optional[str] = Field(
        default=None, serialization_alias="Target Project Info", max_length=3000, json_schema_extra={"column":"AB"}
    )
    Davis_Bacon_Certification__c: Optional[YesNoType] = Field(
        default=None, serialization_alias="Davis Bacon Certification?", json_schema_extra={"column":"AC"}
    )
    Number_of_Direct_Employees__c: Optional[conint(ge=0, le=99999999999)] = Field(
        default=None, serialization_alias="Number of Direct Employees", json_schema_extra={"column":"AD"}
    )
    Number_of_Contractor_Employees__c: Optional[conint(ge=0, le=9999999999)] = Field(
        default=None, serialization_alias="Number of Contractor Employees", json_schema_extra={"column":"AE"}
    )
    Number_of_3rd_Party_Employees__c: Optional[conint(ge=0, le=999999999999)] = Field(
        default=None, serialization_alias="Number of 3rd Party Employees", json_schema_extra={"column":"AF"}
    )
    Any_Wages_Less_Than_Prevailing__c: Optional[YesNoType] = Field(
        default=None, serialization_alias="Any Wages Less Than Prevailing?", json_schema_extra={"column":"AG"}
    )
    Wages_and_benefits__c: Optional[str] = Field(
        default=None,
        serialization_alias="Wages and benefits of workers on the project by classification",
        max_length=3000,
        json_schema_extra={"column":"AH"}
    )
    Project_Labor_Certification__c: Optional[YesNoType] = Field(
        default=None, serialization_alias="Project Labor Certification?", json_schema_extra={"column":"AI"}
    )
    Assurance_of_Adequate_Labor__c: Optional[str] = Field(
        default=None,
        serialization_alias="Assurance of Adequate Labor?",
        max_length=3000,
        json_schema_extra={"column":"AJ"}
    )
    Minimizing_Risks__c: Optional[str] = Field(
        default=None, serialization_alias="Minimizing Risks?", max_length=3000, json_schema_extra={"column":"AK"}
    )
    Safe_and_Healthy_Workplace__c: Optional[str] = Field(
        default=None,
        serialization_alias="Explain Safe and Healthy Workplace",
        max_length=3000,
        json_schema_extra={"column":"AL"}
    )
    Adequate_Wages__c: Optional[YesNoType] = Field(
        default=None, serialization_alias="Adequate Wages?", json_schema_extra={"column":"AM"}
    )
    Project_Labor_Agreement__c: Optional[YesNoType] = Field(
        default=None, serialization_alias="Project Labor Agreement?", json_schema_extra={"column":"AN"}
    )
    Prioritize_Local_Hires__c: Optional[YesNoType] = Field(
        default=None, serialization_alias="Prioritize Local Hires?", json_schema_extra={"column":"AO"}
    )
    Community_Benefit_Agreement__c: Optional[YesNoType] = Field(
        default=None, serialization_alias="Community Benefit Agreement?", json_schema_extra={"column":"AP"}
    )
    Description_of_Community_Ben_Agr__c: Optional[str] = Field(
        default=None,
        serialization_alias="Description of Community Ben. Agr.",
        max_length=3000,
        json_schema_extra={"column":"AQ"}
    )

    @validator(
        "Projected_Con_Start_Date__c",
        "Projected_Con_Completion__c",
        "Projected_Init_of_Operations__c",
        "Actual_Con_Start_Date__c",
        "Actual_Con_Completion__c",
        "Actual_operations_date__c",
        pre=True,
    )
    def parse_mm_dd_yyyy_dates(cls, value):
        if isinstance(value, str):
            try:
                return datetime.strptime(value, "%m/%d/%Y")
            except ValueError:
                raise ValueError(f"Date {value} is not in 'mm/dd/yyyy' format.")
        return value


class Project1ARow(BaseProjectRow):
    Technology_Type_Planned__c: TechType = Field(
        ..., serialization_alias="Technology Type (Planned)", json_schema_extra={"column":"AR"}
    )
    Technology_Type_Actual__c: Optional[TechType] = Field(
        default=None, serialization_alias="Technology Type (Actual)", json_schema_extra={"column":"AS"}
    )
    If_Other_Specify_Planned__c: Optional[str] = Field(
        default=None,
        serialization_alias="If Other, Specify (Planned)?",
        max_length=3000,
        json_schema_extra={"column":"AT"}
    )
    If_Other_Specify_Actual__c: Optional[str] = Field(
        default=None,
        serialization_alias="If Other, Specify (Actual?)?",
        max_length=3000,
        json_schema_extra={"column":"AU"}
    )
    Total_Miles_Planned__c: conint(ge=0, le=999999999) = Field(
        ..., serialization_alias="Total Miles of Fiber Deployed (Planned)", json_schema_extra={"column":"AV"}
    )
    Total_Miles_Actual__c: Optional[conint(ge=0, le=999999999)] = Field(
        default=None, serialization_alias="Total Miles of Fiber Deployed (Actual)", json_schema_extra={"column":"AW"}
    )
    Locations_Served_Planned__c: conint(ge=0, le=999999999) = Field(
        ..., serialization_alias="A) Total Number of Locations Served (Planned)", json_schema_extra={"column":"AX"}
    )
    Locations_Served_Actual__c: Optional[conint(ge=0, le=999999999)] = Field(
        default=None, serialization_alias="A) Total Number of Locations Served (Actual)", json_schema_extra={"column":"AY"}
    )
    X25_3_Mbps_or_below_Planned__c: conint(ge=0, le=999999999) = Field(
        ..., serialization_alias="B) Less than 25/3 Mbps (Planned)", json_schema_extra={"column":"AZ"}
    )
    X25_3_Mbps_and_100_20_Mbps_Planned__c: conint(ge=0, le=999999999) = Field(
        ..., serialization_alias="C) 25/3 Mbps and 100/20 Mbps (Planned)", json_schema_extra={"column":"BA"}
    )
    Minimum_100_100_Mbps_Planned__c: conint(ge=0, le=999999999) = Field(
        ..., serialization_alias="D) Minimum 100/100 Mbps (Planned) ", json_schema_extra={"column":"BB"}
    )
    Minimum_100_100_Mbps_Actual__c: Optional[conint(ge=0, le=999999999)] = Field(
        default=None, serialization_alias="D) Minimum 100/100 Mbps (Actual) ", json_schema_extra={"column":"BC"}
    )
    X100_20_Mbps_to_100_100_Mbps_Planned__c: conint(ge=0, le=999999999) = Field(
        ..., serialization_alias="E) 100/20 Mbps to 100/100 Mbps (Planned)", json_schema_extra={"column":"BD"}
    )
    X100_20_Mbps_to_100_100_Mbps_Actual__c: Optional[conint(ge=0, le=999999999)] = (
        Field(
            default=None, serialization_alias="E) 100/20 Mbps to 100/100 Mbps (Actual)", json_schema_extra={"column":"BE"}
        )
    )
    Explanation_of_Discrepancy__c: Optional[str] = Field(
        default=None,
        serialization_alias="Explanation of Discrepancy (Location by Speed)",
        max_length=3000,
        json_schema_extra={"column":"BF"}
    )
    Number_of_Locations_Planned__c: conint(ge=0, le=999999999) = Field(
        ...,
        serialization_alias="F) Total Number of Locations Served by Type - Residential (Planned)",
        json_schema_extra={"column":"BG"}
    )
    Number_of_Locations_Actual__c: Optional[conint(ge=0, le=999999999)] = Field(
        default=None,
        serialization_alias="F) Total Number of Locations Served by Type - Residential (Actual)",
        json_schema_extra={"column":"BH"}
    )
    Housing_Units_Planned__c: conint(ge=0, le=999999999) = Field(
        ..., serialization_alias="G) Total Housing Units (Planned)", json_schema_extra={"column":"BI"}
    )
    Housing_Units_Actual__c: Optional[conint(ge=0, le=999999999)] = Field(
        default=None, serialization_alias="G) Total Housing Units (Actual)", json_schema_extra={"column":"BJ"}
    )
    Number_of_Bus_Locations_Planned__c: conint(ge=0, le=999999999) = Field(
        ...,
        serialization_alias="H) Total Number of Locations Served by Type - Business (Planned)",
        json_schema_extra={"column":"BK"}
    )
    Number_of_Bus_Locations_Actual__c: Optional[conint(ge=0, le=999999999)] = Field(
        default=None,
        serialization_alias="H) Total Number of Locations Served by Type - Business (Actual)",
        json_schema_extra={"column":"BL"}
    )
    Number_of_CAI_Planned__c: conint(ge=0, le=999999999) = Field(
        ...,
        serialization_alias="I) Total Number of Locations Served by Type - Community Anchor Institution (Planned)",
        json_schema_extra={"column":"BM"}
    )
    Number_of_CAI_Actual__c: Optional[conint(ge=0, le=999999999)] = Field(
        default=None,
        serialization_alias="I) Total Number of Locations Served by Type - Community Anchor Institution (Actual)",
        json_schema_extra={"column":"BN"}
    )
    Explanation_Planned__c: Optional[str] = Field(
        default=None, serialization_alias="Explanation (Planned)", max_length=3000, json_schema_extra={"column":"BO"}
    )
    Affordable_Connectivity_Program_ACP__c: YesNoType = Field(
        ..., serialization_alias="Affordable Connectivity Program (ACP)?", json_schema_extra={"column":"BP"}
    )


class AddressFields(BaseModel):
    Street_1_Planned__c: str = Field(
        ..., serialization_alias="Street 1 (Planned)", max_length=40, json_schema_extra={"column":"BQ"}
    )
    Street_2_Planned__c: str = Field(
        default=None, serialization_alias="Street 2 (Planned)", max_length=40, json_schema_extra={"column":"BR"}
    )
    Same_Address__c: YesNoType = Field(default=None, serialization_alias="Same Address", json_schema_extra={"column":"BS"})
    Street_1_Actual__c: str = Field(
        default=None, serialization_alias="Street 1 (Actual)", max_length=40, json_schema_extra={"column":"BT"}
    )
    Street_2_Actual__c: str = Field(
        default=None, serialization_alias="Street 2 (Actual)", max_length=40, json_schema_extra={"column":"BU"}
    )
    City_Planned__c: str = Field(
        ..., serialization_alias="City (Planned)", max_length=40, json_schema_extra={"column":"BV"}
    )
    City_Actual__c: str = Field(
        default=None, serialization_alias="City (Actual)", max_length=40, json_schema_extra={"column":"BW"}
    )
    State_Planned__c: StateAbbreviation = Field(
        ..., serialization_alias="State (Planned)", json_schema_extra={"column":"BX"}
    )
    State_Actual__c: StateAbbreviation = Field(
        default=None, serialization_alias="State (Actual)", json_schema_extra={"column":"BY"}
    )
    Zip_Code_Planned__c: str = Field(
        ..., serialization_alias="Zip Code (Planned)", max_length=5, json_schema_extra={"column":"BZ"}
    )
    Zip_Code_Actual__c: str = Field(
        default=None, serialization_alias="Zip Code (Actual)", max_length=5, json_schema_extra={"column":"CA"}
    )


class Project1BRow(BaseProjectRow, AddressFields):
    Laptops_Planned__c: conint(ge=0, le=9999999999) = Field(
        ..., serialization_alias="Laptops (Planned)", json_schema_extra={"column":"CB"}
    )
    Laptops_Actual__c: conint(ge=0, le=9999999999) = Field(
        default=None, serialization_alias="Laptops (Actual)", json_schema_extra={"column":"CC"}
    )
    Laptops_Expenditures_Planned__c: condecimal(max_digits=13, decimal_places=2) = (
        Field(..., serialization_alias="Laptops Expenditure (Planned)", json_schema_extra={"column":"CD"})
    )
    Laptops_Expenditures_Actual__c: condecimal(max_digits=13, decimal_places=2) = Field(
        default=None, serialization_alias="Laptops Expenditure (Actual)", json_schema_extra={"column":"CE"}
    )
    Tablets_Planned__c: conint(ge=0, le=9999999999) = Field(
        ..., serialization_alias="Tablets (Planned)", json_schema_extra={"column":"CF"}
    )
    Tablets_Actual__c: conint(ge=0, le=9999999999) = Field(
        default=None, serialization_alias="Tablets (Actual)", json_schema_extra={"column":"CG"}
    )
    Tablet_Expenditures_Planned__c: condecimal(max_digits=13, decimal_places=2) = Field(
        ..., serialization_alias="Tablets Expenditure (Planned)", json_schema_extra={"column":"CH"}
    )
    Tablets_Expenditures_Actual__c: condecimal(max_digits=13, decimal_places=2) = Field(
        default=None, serialization_alias="Tablets Expenditure (Actual)", json_schema_extra={"column":"CI"}
    )
    Desktop_Computers_Planned__c: conint(ge=0, le=9999999999) = Field(
        ..., serialization_alias="Desktop Computers (Planned)", json_schema_extra={"column":"CJ"}
    )
    Desktop_Computers_Actual__c: conint(ge=0, le=9999999999) = Field(
        default=None, serialization_alias="Desktop Computers (Actual)", json_schema_extra={"column":"CK"}
    )
    Desktop_Computers_Expenditures_Planned__c: condecimal(
        max_digits=13, decimal_places=2
    ) = Field(..., serialization_alias="Desktop Computers Expenditure (Planned)", json_schema_extra={"column":"CL"})
    Desktop_Computers_Expenditures_Actual__c: condecimal(
        max_digits=13, decimal_places=2
    ) = Field(
        default=None, serialization_alias="Desktop Computers Expenditure (Actual)", json_schema_extra={"column":"CM"}
    )
    Public_WiFi_Planned__c: conint(ge=0, le=9999999999) = Field(
        ..., serialization_alias="Public WiFi (Planned)", json_schema_extra={"column":"CN"}
    )
    Public_WiFi_Actual__c: conint(ge=0, le=9999999999) = Field(
        default=None, serialization_alias="Public WiFi (Actual)", json_schema_extra={"column":"CO"}
    )
    Public_WiFi_Expenditures_Planned__c: condecimal(max_digits=13, decimal_places=2) = (
        Field(..., serialization_alias="Public Wifi Expenditures (Planned)", json_schema_extra={"column":"CP"})
    )
    Public_WiFi_Expenditures_Actual__c: condecimal(max_digits=13, decimal_places=2) = (
        Field(default=None, serialization_alias="Public Wifi Expenditures (Actual)", json_schema_extra={"column":"CQ"})
    )
    Other_Devices_Planned__c: conint(ge=0, le=9999999999) = Field(
        ..., serialization_alias="Other Devices (Planned)", json_schema_extra={"column":"CR"}
    )
    Other_Devices_Actual__c: conint(ge=0, le=9999999999) = Field(
        default=None, serialization_alias="Other Devices (Actual)", json_schema_extra={"column":"CS"}
    )
    Other_Expenditures_Planned__c: condecimal(max_digits=7, decimal_places=2) = Field(
        ..., serialization_alias="Other Expenditures (Planned)", json_schema_extra={"column":"CT"}
    )
    Other_Expenditures_Actual__c: condecimal(max_digits=7, decimal_places=2) = Field(
        default=None, serialization_alias="Other Expenditures (Actual)", json_schema_extra={"column":"CU"}
    )
    Explanation_of_Other_Expend__c: str = Field(
        default=None,
        serialization_alias="Explanation of Other Expenditures",
        max_length=3000,
        json_schema_extra={"column":"CV"}
    )
    Number_of_Users_Planned__c: conint(ge=0, le=9999999999) = Field(
        ..., serialization_alias="Number of Users (Planned)", json_schema_extra={"column":"CW"}
    )
    Number_of_Users_Actual__c: conint(ge=0, le=9999999999) = Field(
        default=None, serialization_alias="Number of Users (Actual)", json_schema_extra={"column":"CX"}
    )
    Brief_Narrative_Planned__c: str = Field(
        ..., serialization_alias="Brief Narrative (Planned)", max_length=3000, json_schema_extra={"column":"CY"}
    )
    Brief_Narrative_Actual__c: str = Field(
        default=None, serialization_alias="Brief Narrative (Actual)", max_length=3000, json_schema_extra={"column":"CZ"}
    )
    Measurement_of_Effectiveness__c: YesNoType = Field(
        ..., serialization_alias="Measurement of Effectiveness?", json_schema_extra={"column":"DA"}
    )


class Project1CRow(BaseProjectRow, AddressFields):
    Type_of_Investment__c: str = Field(
        default=None, serialization_alias="Type of Investment", json_schema_extra={"column":"DB"}
    )
    Additional_Address__c: str = Field(
        default=None, serialization_alias="Additional Addresses", max_length=32000, json_schema_extra={"column":"DC"}
    )
    Classrooms_Planned__c: conint(ge=0, le=9999999999) = Field(
        default=None, serialization_alias="Classrooms (Planned)", json_schema_extra={"column":"DD"}
    )
    Classrooms_Actual__c: conint(ge=0, le=9999999999) = Field(
        default=None, serialization_alias="Classrooms (Actual)", json_schema_extra={"column":"DE"}
    )
    Computer_labs_Planned__c: conint(ge=0, le=9999999999) = Field(
        default=None, serialization_alias="Computer labs (Planned)", json_schema_extra={"column":"DF"}
    )
    Computer_labs_Actual__c: conint(ge=0, le=9999999999) = Field(
        default=None, serialization_alias="Computer labs (Actual)", json_schema_extra={"column":"DG"}
    )
    Multi_purpose_Spaces_Planned__c: conint(ge=0, le=9999999999) = Field(
        default=None, serialization_alias="Multi-purpose Spaces (Planned)", json_schema_extra={"column":"DH"}
    )
    Multi_purpose_Spaces_Actual__c: conint(ge=0, le=9999999999) = Field(
        default=None, serialization_alias="Multi-purpose Spaces (Actual)", json_schema_extra={"column":"DI"}
    )
    Telemedicine_Rooms_Planned__c: conint(ge=0, le=9999999999) = Field(
        default=None, serialization_alias="Telemedicine Rooms (Planned)", json_schema_extra={"column":"DJ"}
    )
    Telemedicine_Rooms_Actual__c: conint(ge=0, le=9999999999) = Field(
        default=None, serialization_alias="Telemedicine Rooms (Actual)", json_schema_extra={"column":"DK"}
    )
    Other_Capital_Assets_Planned__c: conint(ge=0, le=9999999999) = Field(
        default=None, serialization_alias="Other Capital Assets (Planned)", json_schema_extra={"column":"DL"}
    )
    Other_Capital_Assets_Actual__c: conint(ge=0, le=9999999999) = Field(
        default=None, serialization_alias="Other Capital Assets (Actual)", json_schema_extra={"column":"DM"}
    )
    Type_and_Features__c: str = Field(
        default=None, serialization_alias="Type and Features", max_length=3000, json_schema_extra={"column":"DN"}
    )
    Total_square_footage_Planned__c: conint(ge=0, le=9999999999) = Field(
        default=None, serialization_alias="Total square footage (Planned)", json_schema_extra={"column":"DO"}
    )
    Total_square_footage_Actual__c: conint(ge=0, le=9999999999) = Field(
        default=None, serialization_alias="Total square footage (Actual)", json_schema_extra={"column":"DP"}
    )
    Total_Number_of_Users_Actual__c: conint(ge=0, le=9999999999) = Field(
        default=None, serialization_alias="Total Number of Users (Actual)", json_schema_extra={"column":"DQ"}
    )
    Further_Explanation__c: str = Field(
        default=None, serialization_alias="Further Explanation", max_length=2000, json_schema_extra={"column":"DR"}
    )
    Access_to_Public_Transit__c: YesNoType = Field(
        ..., serialization_alias="Access to Public Transit?", json_schema_extra={"column":"DS"}
    )


class SubrecipientRow(BaseModel):
    model_config = ConfigDict(coerce_numbers_to_str=True, loc_by_alias=False)

    Name: str = Field(..., serialization_alias="Subrecipient Name", max_length=80, json_schema_extra={"column":"C"})
    EIN__c: str = Field(
        ...,
        serialization_alias="Subrecipient Tax ID Number (TIN)",
        min_length=9,
        max_length=9,
        json_schema_extra={"column":"D"}
    )
    Unique_Entity_Identifier__c: str = Field(
        ...,
        serialization_alias="Unique Entity Identifier (UEI)",
        min_length=12,
        max_length=12,
        json_schema_extra={"column":"E"}
    )
    POC_Name__c: str = Field(..., serialization_alias="POC Name", max_length=100, json_schema_extra={"column":"F"})
    POC_Phone_Number__c: str = Field(
        ..., serialization_alias="POC Phone Number", max_length=10, json_schema_extra={"column":"G"}
    )
    POC_Email_Address__c: str = Field(
        ..., serialization_alias="POC Email Address", max_length=80, json_schema_extra={"column":"H"}
    )
    Zip__c: str = Field(..., serialization_alias="Zip5", max_length=5, json_schema_extra={"column":"I"})
    Zip_4__c: str = Field(default=None, serialization_alias="Zip4", max_length=4, json_schema_extra={"column":"J"})
    Address__c: str = Field(..., serialization_alias="Address Line 1", max_length=40, json_schema_extra={"column":"K"})
    Address_2__c: str = Field(
        default=None, serialization_alias="Address Line 2", max_length=40, json_schema_extra={"column":"L"}
    )
    Address_3__c: str = Field(
        default=None, serialization_alias="Address Line 3", max_length=40, json_schema_extra={"column":"M"}
    )
    City__c: str = Field(..., serialization_alias="City", max_length=100, json_schema_extra={"column":"N"})
    State_Abbreviated__c: StateAbbreviation = Field(
        ..., serialization_alias="State Abbreviated", json_schema_extra={"column":"O"}
    )


class Version(Enum):
    V2023_12_12 = "v:20231212"
    V2024_01_07 = "v:20240107"
    V2024_04_01 = "v:20240401"


class ProjectType(str, Enum):
    _1A = "1A"
    _1B = "1B"
    _1C = "1C"

    @classmethod
    def from_project_name(cls, project_name: str) -> "ProjectType":
        for project_type in cls:
            if project_type.value == project_name:
                return project_type
        raise ValueError(f"Project name '{project_name}' is not a recognized project type.")


SCHEMA_BY_PROJECT = {
    ProjectType._1A: Project1ARow,
    ProjectType._1B: Project1BRow,
    ProjectType._1C: Project1CRow,
}
NAME_BY_PROJECT = {
    ProjectType._1A: "1A-Broadband Infrastructure",
    ProjectType._1B: "1B-Digital Connectivity Technology",
    ProjectType._1C: "1C-Multi-Purpose Community Facility",
}

METADATA_BY_SHEET = {
    "Cover": {
        "header_range": "A1:B1",
        "min_row": 2,
        "max_row": 2,
        "min_col": 1,
        "max_col": 2,
    },
    "Subrecipients": {
        "header_range": "C3:O3",
        "min_row": 13,
        "max_row": None,
        "min_col": 3,
        "max_col": 16,
    },
    "Project": {
        "header_range": "C3:DS3",
        "min_row": 13,
        "max_row": None,
        "min_col": 3,
        "max_col": 123,
    },
}


class LogicSheetVersion(BaseModel):
    version: Version = Field(...)


class CoverSheetRow(BaseModel):
    model_config = ConfigDict(loc_by_alias=False)

    project_use_code: str = Field(..., alias="Project Use Code", json_schema_extra={"column":"A"})
    project_use_name: str = Field(..., alias="Project Use Name", json_schema_extra={"column":"B"})

    @validator("project_use_name")
    def validate_code_name_pair(cls, v, values, **kwargs):
        project_use_code = values.get("project_use_code")
        expected_name = NAME_BY_PROJECT.get(project_use_code)

        if not expected_name:
            raise ValueError(
                f"Project use code '{project_use_code}' is not recognized."
            )
        if expected_name != v:
            raise ValueError(
                f"Project use code '{project_use_code}' does not match '{v}'. Expected '{expected_name}'."
            )

        return v
