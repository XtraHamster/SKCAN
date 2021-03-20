mkdir -p ~/.streamlit/

echo "\
[general]\n\
email = \"martinkrecek98@seznam.cz\"\n\
" > ~/.streamlit/credentials.toml

echo "\
[server]\n\
headless = true\n\
enableCORS=false\n\
port = $PORT\n\
" > ~/.streamlit/config.toml