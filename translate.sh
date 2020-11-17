pybabel extract -F babel.cfg -k _l -o messages.pot .
pybabel update -i messages.pot -d app/translations
pybabel compile -d app/translations compiling catalog app/translations/es/LC_MESSAGES/messager.po to app/translations/es/LC_MESSAGES/messages.mo
