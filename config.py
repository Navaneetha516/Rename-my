# Don't Remove Credit @VJ_Botz
# Subscribe YouTube Channel For Amazing Bot @Tech_VJ
# Ask Doubt on telegram @KingVJ01


import re, os

id_pattern = re.compile(r'^.\d+$') 

API_ID = os.environ.get("API_ID", "20053544")

API_HASH = os.environ.get("API_HASH", "f26c4d28081c11e0c48707143f7bb5b1")

BOT_TOKEN = os.environ.get("BOT_TOKEN", "6564619822:AAFPE4TB9gNNmDzY700JZ-wJSjXIMfUtBcU") 

FORCE_SUB = os.environ.get("FORCE_SUB", "-1001688675040") 

             # Don't Remove Credit @Movie_Time_HD_1
             # Subscribe YouTube Channel For Amazing Bot @Tech_VJ
             # Ask Doubt on telegram @KingVJ01

DB_NAME = os.environ.get("DB_NAME", "renamevjbot")     

DB_URL = os.environ.get("DB_URL", "mongodb+srv://MovieTimeHD1:MovieTimeHD1@cluster0.trfqzij.mongodb.net/")
 
FLOOD = int(os.environ.get("FLOOD", "10"))

START_PIC = os.environ.get("START_PIC", "https://te.legra.ph/file/119729ea3cdce4fefb6a1.jpg")

ADMIN = [int(admin) if id_pattern.search(admin) else admin for admin in os.environ.get('ADMIN', '1439022100').split()]

PORT = os.environ.get("PORT", "8080")

# Don't Remove Credit @VJ_Botz
# Subscribe YouTube Channel For Amazing Bot @Tech_VJ
# Ask Doubt on telegram @KingVJ01
