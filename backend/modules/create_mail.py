def generate_mail(username, url):
    return f"""
<!DOCTYPE html>
<html lang="ru">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
    <!-- Google fonts -->
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link
        href="https://fonts.googleapis.com/css2?family=Roboto:ital,wght@0,100;0,300;0,400;0,500;0,700;0,900;1,100;1,300;1,400;1,500;1,700;1,900&display=swap"
        rel="stylesheet">
</head>

<body style="margin: 0; height: 100%;
font-family: Roboto, sans-serif; font-weight: 400; font-style: normal;">
    <div class="wrapper" style=" width: 100%;
    height: 100%;">
        <header style="background-color: #005CC9;
        user-select: none;
        padding: 30px;">
            <h1 style="  margin: 0;
            text-align: center;
            font-size: 2em;
            font-weight: bold;
            color: white;">
                Добро пожаловать в WISH EDU!
            </h1>
        </header>
        <main style="  display: flex;
        justify-content: center;
        flex-direction: column;">
            <img src="https://cdn.althgamer.ru/assets/static/images/opened-letter-success_2000x2000.webp" alt="📧"
                style=" width: 256px;
            height: 256px;
            margin-top: 40px;
            margin-inline: auto;
            user-select: none;
            pointer-events: none;" />
            <div class="letter" style="width: 60%;
            margin-inline: auto;
            margin-bottom: 10px;
            text-align: center;">
                <h2>
                    Приветствуем {{ USERNAME }},
                </h2>
                <p style="margin-block: 20px;">
                    Благодарим за регистрация аккаунта в экосистеме WISH EDU!
                </p>
                <p>
                    Перед тем как начать полноценно пользоваться платформой, необходимо подтвердить Вашу почту.
                </p>
                <a href="{ url }" style="display: inline-block; width: 170px; height: 60px; margin-inline: auto; margin-top: 50px; text-decoration: none; font-size: 1em; color: white; background-color: #005CC9; text-align: center; line-height: 60px;">
                    Подтвердить почту
                </a>
            </div>
        </main>
    </div>
</body>

</html>
"""