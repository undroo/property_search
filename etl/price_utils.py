# Mapping to convert price data from gov into a standardised format
record_a_mapping = [
    "Record Type",
    "File Type",
    "District Code"
]

record_b_mapping = [
    "Record Type",
    "District Code",
    "Property ID",
    "Sale Counter", # Not important
    "Download Date", # Not import
    "Property Name",
    "Unit number",
    "House number",
    "Street name",
    "Suburb",
    "Postcode",
    "Area",
    "Area type", #either M metres or H hectares
    "Contract Date", # format is CCYYMMDD
    "Settlement Date", # format is CCYYMMDD
    "Price",
    "Zone", #
    "Nature of Property", # V = Vacant, R = Residence, 3 = Other
    "Primary Purpose", # only when nature of property is Other
    "Strata Lot Number",
    "Comp Code", # Not important
    "Sale Code", # Not important
    "Percentage of Interest of Sale", # Unsure
    "Dealing Number", # Not important
]

record_c_mapping = [
    "Record Type",
    "District Code",
    "Property ID",
    "Sale Counter", # Not important
    "Download Date", # Not important
    "Legal Description",
]

record_d_mapping = [
    "Record Type",
    "District Code",
    "Property ID",
]

record_z_mapping = [
    "Record Type",
    "Total Records",
    "Total B Records",
    "Total C Records",
    "Total D Records", # Not important
]

# 2001 - Current Record Type mapping
record_mapping = { 
    "A": record_a_mapping,
    "B": record_b_mapping,
    "C": record_c_mapping,
    "D": record_d_mapping,
    "Z": record_z_mapping,
}

archival_record_a_mapping = [
    "Record Type",
    "District Code"
]

archival_record_b_mapping = [
    "Record Type",
    "District Code",
    "Source",
    "Valuation",
    "Property ID",
    "Unit number",
    "House number",
    "Street name",
    "Suburb",
    "Postcode",
    "Contract Date", # format is CCYYMMDD
    "Price",
    "Land description",
    "Area",
    "Area type", #either M metres or H hectares
    "Dimensions",
    "comp_code", # Not important
    "Zone", #?
    "Vendor name", # Blanked
    "Purchaser name", # Blanked
]

# District Code mapping and function

def get_district_code(district):
    if district in district_code_mapping:
        return district_code_mapping[district]
    else:
        return None

district_code_mapping = { # 3 digit number linking to a district code in NSW
    "050": "ALBURY",
    "257": "ARMIDALE REGIONAL",
    "148": "BALLINA",
    "230": "BALRANALD",
    "608": "BATHURST REGIONAL",
    "276": "BAYSIDE",
    "018": "BEGA VALLEY",
    "149": "BELLINGEN",
    "051": "BERRIGAN",
    "214": "BLACKTOWN",
    "231": "BLAND",
    "118": "BLAYNEY",
    "216": "BLUE MOUNTAINS",
    "232": "BOGAN",
    "239": "BOURKE",
    "233": "BREWARRINA",
    "234": "BROKEN HILL",
    "137": "BURWOOD",
    "150": "BYRON",
    "109": "CABONNE",
    "217": "CAMDEN",
    "218": "CAMPBELLTOWN",
    "139": "CANADA BAY",
    "258": "CANTERBURY-BANKSTOWN",
    "052": "CARRATHOOL",
    "259": "CENTRAL COAST",
    "235": "CENTRAL DARLING",
    "001": "CESSNOCK",
    "260": "CITY OF PARRAMATTA",
    "708": "CITY OF SYDNEY",
    "303": "CLARENCE VALLEY",
    "236": "COBAR",
    "152": "COFFS HARBOUR",
    "054": "COOLAMON",
    "238": "COONAMBLE",
    "265": "COOTAMUNDRA-GUNDAGAI REGIONAL",
    "042": "COWRA",
    "261": "CUMBERLAND",
    "275": "DUBBO REGIONAL",
    "002": "DUNGOG",
    "262": "EDWARD RIVER",
    "097": "EUROBODALLA",
    "220": "FAIRFIELD",
    "263": "FEDERATION",
    "117": "FORBES",
    "264": "GEORGES RIVER",
    "240": "GILGANDRA",
    "302": "GLEN INNES SEVERN",
    "529": "GOULBURN MULWAREE",
    "560": "GREATER HUME",
    "074": "GRIFFITH",
    "187": "GUNNEDAH",
    "300": "GWYDIR",
    "219": "HAWKESBURY",
    "243": "HAY",
    "266": "HILLTOPS",
    "082": "HORNSBY",
    "083": "HUNTERS HILL",
    "267": "INNER WEST",
    "188": "INVERELL",
    "061": "JUNEE",
    "157": "KEMPSEY",
    "098": "KIAMA",
    "084": "KU-RING-GAI",
    "158": "KYOGLE",
    "244": "LACHLAN",
    "004": "LAKE MACQUARIE",
    "085": "LANE COVE",
    "065": "LEETON",
    "159": "LISMORE",
    "222": "LITHGOW",
    "223": "LIVERPOOL",
    "301": "LIVERPOOL PLAINS",
    "066": "LOCKHART",
    "005": "MAITLAND",
    "620": "MID WESTERN REGIONAL",
    "268": "MID-COAST",
    "192": "MOREE PLAINS",
    "087": "MOSMAN",
    "269": "MURRAY RIVER",
    "270": "MURRUMBIDGEE",
    "007": "MUSWELLBROOK",
    "164": "NAMBUCCA",
    "247": "NARRABRI",
    "070": "NARRANDERA",
    "251": "NARROMINE",
    "008": "NEWCASTLE",
    "088": "NORTH SYDNEY",
    "271": "NORTHERN BEACHES",
    "123": "OBERON",
    "124": "ORANGE",
    "116": "PARKES",
    "224": "PENRITH",
    "656": "PORT MACQUARIE-HASTINGS",
    "010": "PORT STEPHENS",
    "272": "QUEANBEYAN-PALERANG REGIONAL",
    "207": "RANDWICK",
    "151": "RICHMOND VALLEY",
    "090": "RYDE",
    "100": "SHELLHARBOUR",
    "101": "SHOALHAVEN",
    "012": "SINGLETON",
    "273": "SNOWY MONARO REGIONAL",
    "274": "SNOWY VALLEYS",
    "143": "STRATHFIELD",
    "144": "SUTHERLAND",
    "666": "TAMWORTH REGIONAL",
    "538": "TEMORA",
    "250": "TENTERFIELD",
    "081": "THE HILLS SHIRE",
    "171": "TWEED",
    "511": "UPPER HUNTER",
    "526": "UPPER LACHLAN",
    "199": "URALLA",
    "575": "WAGGA WAGGA",
    "252": "WALCHA",
    "253": "WALGETT",
    "254": "WARREN",
    "537": "WARRUMBUNGLE",
    "209": "WAVERLEY",
    "043": "WEDDIN",
    "255": "WENTWORTH",
    "092": "WILLOUGHBY",
    "102": "WINGECARRIBEE",
    "226": "WOLLONDILLY",
    "103": "WOLLONGONG",
    "210": "WOOLLAHRA",
    "528": "YASS VALLEY",
    "902": "UNINCORPORATED AREA",
    "903": "UNINCORPORATED SYDNEY HARBOUR",

}