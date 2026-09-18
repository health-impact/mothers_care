import os
import json
from google import genai

# جلب المفتاح
api_key = os.environ.get("GEMINI_API_KEY")

# إعداد العميل
client = genai.Client(api_key=api_key)

prompt = """
أنت مستشار طبي متخصص في صحة الأم والطفل والولادة القيصرية، بالاعتماد على توصيات (WHO, ACOG, AAP).
قُم بكتابة نصيحة أسبوعية حصرية ومفيدة جداً للأمهات.
يجب أن ترجع النتيجة بصيغة JSON فقط بالهيكل التالي بدون أي كود آخر:
{
    "date": "التاريخ الحالي بالعربي",
    "title": "عنوان جذاب للنصيحة الأسبوعية",
    "category": "إما: الولادة القيصرية أو صحة الأم أو رعاية الطفل",
    "content": "نص النصيحة الشامل المكتوب بلغة عربية بسيطة ودافئة ومباشرة (حوالي 3-4 أسطر).",
    "source": "ACOG أو WHO أو AAP حسب التوصية"
}
"""

# استخدام النموذج الصحيح والمحدث
response = client.models.generate_content(
    model='gemini-2.5-flash',
    contents=prompt,
)

clean_json = response.text.replace("```json", "").replace("```", "").strip()

# إنشاء مجلد data وحفظ البيانات
os.makedirs("data", exist_ok=True)
with open("data/weekly.json", "w", encoding="utf-8") as f:
    f.write(clean_json)

print("تم تحديث ملف data/weekly.json بنجاح!")
