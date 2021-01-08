import os
import uvicorn

if __name__ == '__main__':
    port = os.environ.get('PORT', 5000)
    uvicorn.run('superres_api.main:app', host='0.0.0.0', port=port)
