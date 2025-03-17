echo 'hello'

rm -f cmeraz-func.zip

cd src

zip -r ../cmeraz-func.zip * -x tests/ .funcignore local.settings.json @

cd ../

az functionapp deployment source config-zip -g rg-cmeraz-func -n cmeraz-func --src cmeraz-func.zip