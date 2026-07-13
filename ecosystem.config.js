module.exports = {
  apps: [
    {
      name: "crypto-flow-scanner",
      script: "main.py",
      interpreter: "/opt/crypto-flow-scanner/venv/bin/python",
      cwd: "/opt/crypto-flow-scanner",
      autorestart: true,
      watch: false,
      max_memory_restart: "1G",
      env: {
        PYTHONUNBUFFERED: "1"
      }
    }
  ]
}