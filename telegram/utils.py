import httpx

from telegram import schemas
from environs import Env

env = Env()
env.read_env()

token = env.str("BOT_TOKEN")

MESSAGES = {
    'uz': {
        'DRAFT': "⚠️ Arizangiz qoralama holatida. Iltimos, ko'rib chiqib arizangizni yuboring!",
        'SUBMITTED': "☑️ Arizangiz yuborilgan. Iltimos, natijani kuting!",
        'REJECTED': "❌ Arizangiz rad etildi. Iltimos, ko'rib chiqib arizangizni qayta yuboring!",
        'ACCEPTED': "✅ Arizangiz qabul qilindi. Quyidagi \"🧑‍💻 Imtihon topshirish\" tugmasini bosib imtihon topshirishingiz mumkin!",
        'EXAMINED': "🔄 Imtihon topshirildi. Iltimos, natijani kuting!",
        'FAILED': "😔 Imtihondan o'ta olmadingiz. Imtihon topshirish uchun 2 marta imkoniyat beriladi. Shuning uchun sizga imtihon topshirish uchun yana imkoniyat beriladi! Quyidagi \"🧑‍💻 Imtihon topshirish\" tugmasini bosib imtihon topshirishingiz mumkin!",
        'PASSED': "🥳 Siz Fan va texnologiyalar universitetiga tavsiya etildingiz. Quyidagi \"📥 Shartnomani olish\" tugmasi orqali kontakt shartnoma faylini yuklab olishingiz mumkin.",
    },
    'ru': {
        'DRAFT': "⚠️ Ваша заявка в черновике. Пожалуйста, проверьте и отправьте вашу заявку!",
        'SUBMITTED': "☑️ Ваша заявка отправлена. Пожалуйста, ожидайте результат!",
        'REJECTED': "❌ Ваша заявка отклонена. Пожалуйста, проверьте и повторно отправьте вашу заявку!",
        'ACCEPTED': "✅ Ваша заявка принята. Вы можете сдать экзамен, нажав кнопку \"🧑‍💻 Сдать экзамен\" ниже!",
        'EXAMINED': "🔄 Экзамен сдан. Пожалуйста, ожидайте результат!",
        'FAILED': "😔 Вы не сдали экзамен. Вам предоставляется 2 попытки для сдачи экзамена. Поэтому у вас будет еще одна попытка сдать экзамен! Вы можете сдать экзамен, нажав кнопку \"🧑‍💻 Сдать экзамен\" ниже!",
        'PASSED': "🥳 Вы рекомендованы в Университет науки и технологий. Вы можете загрузить контракт, нажав кнопку \"📥 Получить контракт\" ниже.",
    },
    'en': {
        'DRAFT': "⚠️ Your application is in draft status. Please review and submit your application!",
        'SUBMITTED': "☑️ Your application has been submitted. Please wait for the result!",
        'REJECTED': "❌ Your application has been rejected. Please review and resubmit your application!",
        'ACCEPTED': "✅ Your application has been accepted. You can take the exam by clicking the \"🧑‍💻 Take Exam\" button below!",
        'EXAMINED': "🔄 The exam has been taken. Please wait for the result!",
        'FAILED': "😔 You did not pass the exam. You have 2 chances to take the exam. Therefore, you will have another chance to take the exam! You can take the exam by clicking the \"🧑‍💻 Take Exam\" button below!",
        'PASSED': "🥳 You have been recommended to the University of Science and Technology. You can download the contract file by clicking the \"📥 Get Contract\" button below.",
    }
}


async def send_message_via_tg_api(telegram_user: schemas.SendMessage):
    tg_id = telegram_user.tgId
    status = telegram_user.status
    lang = telegram_user.lang

    text = MESSAGES.get(lang, {}).get(status, "Unknown status")
    url = f"https://api.telegram.org/bot{token}/sendMessage"
    params = {
        'chat_id': tg_id,
        'text': text
    }
    async with httpx.AsyncClient() as client:
        response = await client.get(url, params=params)

    if response.status_code == 200:
        return {"message": "Message sent successfully"}
    else:
        return {"message": "Failed to send message", "details": response.json()}
