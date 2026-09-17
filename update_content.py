import os
import json
import google.generativeai as genai
from datetime import datetime

# إعداد مفتاح API
api_key = os.environ.get("GEMINI_API_KEY")
genai.configure(api_key=api_key)

model = genai.GenerativeModel('gemini-1.5-flash')

prompt = """
أنت مستشار طبي متخصص في صحة الأم والطفل والولادة القيصرية، بالاعتماد على توصيات (WHO, ACOG, AAP).
قُم بكتابة نصيحة أسبوعية حصرية ومفيدة جداً للأمهات.
يجب أن ترجع النتيجة بصيغة JSON فقط بالهيكل التالي بدون أي كود آخر:
{
    "date": "التاريخ الحالي بالعربي",
    "title": "عنوان جذاب للنصيحة الأسبوعية",
    "category": "إما: الولادة القيصرية أو صحة الأم أو رعاية الطفل",
    "content": "نص النصيحة الشامل المكتوب بلغة عربية بسيطة ودافئة ومباشرة (حوالي 3-4 أسطر).",
    "fact_vs_myth": "حقيقة أم خرافة طازجة تخص الموضوع",
    "source": "ACOG أو WHO أو AAP حسب التوصية"
}
"""

response = model.generate_content(prompt)
clean_json = response.text.replace("```json", "").replace("```", "").strip()

# إنشاء مجلد data إذا لم يكن موجوداً
os.makedirs("data", exist_ok=True)

# حفظ النتيجة في ملف data/weekly.json
with open("data/weekly.json", "w", encoding="utf-8") as f:
    f.write(clean_json)

print("تم تحديث ملف data/weekly.json بنجاح!")
