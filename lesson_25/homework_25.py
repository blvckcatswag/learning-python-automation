# ===== CSS селекторы =====
css_locators = [
    "a.header_logo",                               # логотип
    "nav.header_nav a.header-link.-active",        # активный пункт меню (Home)
    "nav.header_nav button.header-link",           # About/Contacts
    "button.header-link.-guest",                   # Guest log in
    "button.header_signin",                        # Sign In
    "h1.hero-descriptor_title",                    # заголовок Do more!
    "p.hero-descriptor_descr",                     # описание под заголовком
    "button.hero-descriptor_btn",                  # кнопка Sign up
    "iframe.hero-video_frame",                     # видео
    "div.about-block_picture img.about-picture_img", # картинка в about
    "p.about-block_title",                         # заголовок блока About
    "p.about-block_descr",                         # описание блока About
    "div.contacts h2",                             # заголовок Contacts
    "div.contacts .socials_link.icon-facebook",    # иконка facebook
    "div.contacts .socials_link.icon-telegram",    # иконка telegram
    "div.contacts .socials_link.icon-youtube",     # иконка youtube
    "div.contacts .socials_link.icon-instagram",   # иконка instagram
    "div.contacts .socials_link.icon-linkedin",    # иконка linkedin
    "a.contacts_link.display-4",                   # ссылка ithillel.ua
    "a.contacts_link.h4",                          # email support@ithillel.ua
    "footer.footer",                               # футер
    "footer.footer p:first-child",                 # © 2021 Hillel IT school
    "footer.footer p:last-child",                  # текст про QA courses
    "footer.footer a.footer_logo",                 # логотип в футере
    "footer.footer svg"                            # сам svg логотипа
]

# ===== XPath локаторы =====
xpath_locators = [
    "//a[@class='header_logo']",                                   # логотип
    "//nav[@class='header_nav']//a[contains(text(),'Home')]",      # Home
    "//nav[@class='header_nav']//button[text()='About']",          # About
    "//nav[@class='header_nav']//button[text()='Contacts']",       # Contacts
    "//button[contains(@class,'-guest')]",                         # Guest log in
    "//button[contains(@class,'header_signin')]",                  # Sign In
    "//h1[@class='hero-descriptor_title' and text()='Do more!']",  # заголовок
    "//p[@class='hero-descriptor_descr']",                         # описание
    "//button[@class='hero-descriptor_btn btn btn-primary']",      # Sign up
    "//iframe[@class='hero-video_frame']",                         # видео
    "//div[@class='about-block_picture']//img",                    # картинка
    "//p[@class='about-block_title' and contains(text(),'Log fuel')]", # первый about-блок
    "//p[@class='about-block_title' and contains(text(),'Instructions')]", # второй about-блок
    "//p[@class='about-block_descr']",                             # описания
    "//div[@id='contactsSection']//h2[text()='Contacts']",         # заголовок
    "//div[@class='contacts']//a[contains(@class,'facebook')]",    # facebook
    "//div[@class='contacts']//a[contains(@class,'telegram')]",    # telegram
    "//div[@class='contacts']//a[contains(@class,'youtube')]",     # youtube
    "//div[@class='contacts']//a[contains(@class,'instagram')]",   # instagram
    "//div[@class='contacts']//a[contains(@class,'linkedin')]",    # linkedin
    "//a[@class='contacts_link display-4']",                       # ithillel.ua
    "//a[@class='contacts_link h4' and starts-with(@href,'mailto')]", # email
    "//footer[@class='footer']//p[contains(text(),'© 2021')]",     # © текст
    "//footer[@class='footer']//p[contains(text(),'QA courses')]", # описание
    "//footer[@class='footer']//a[@class='footer_logo']"           # логотип в футере
]
