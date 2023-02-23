from environs import Env

# environs kutubxonasidan foydalanish
env = Env()
env.read_env()
# .env fayl ichidan quyidagilarni o'qiymiz
BOT_TOKEN ="6192418587:AAELHkFwv9QXwK3rcX8SqmN3Cw8NfRqFEqQ"  # Bot toekn
ADMINS =[' 952607746']  # adminlar ro'yxati
IP = env.str("ip")  # Xosting ip manzili
