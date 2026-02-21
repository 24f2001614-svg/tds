# Q20 Ollama/ngrok setup
$env:OLLAMA_ORIGINS="*"
# Start ollama in background
Start-Process ollama "serve"
# Start ngrok
ngrok http 11434 --response-header-add "X-Email: 24f2001614@ds.study.iitm.ac.in" --response-header-add 'Access-Control-Expose-Headers: *' --response-header-add 'Access-Control-Allow-Headers: Authorization,Content-Type,User-Agent,Accept,Ngrok-skip-browser-warning'
