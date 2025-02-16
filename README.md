# Moments

A photo sharing social networking app built with Python and Flask. The example application for the book *[Python Web Development with Flask (2nd edition)](https://helloflask.com/en/book/4)* (《[Flask Web 开发实战（第 2 版）](https://helloflask.com/book/4)》).

Demo: http://moments.helloflask.com

![Screenshot](demo.png)

## Overview
This project enhances the Moments application with ML-powered features, including:
1. Alternative Text Generation: Uses Azure Computer Vision API to generate image descriptions.
2. Image Search with Object Detection: Automatically tags images based on detected objects, enabling search functionality.

## Installation

Clone the repo:

```
$ git clone https://github.com/greyli/moments
$ cd moments
```

Install dependencies with [PDM](https://pdm.fming.dev):

```
$ pdm install
```

> [!TIP]
> If you don't have PDM installed, you can create a virtual environment with `venv` and install dependencies with `pip install -r requirements.txt`.

Install python-dotenv (code loads API keys from a .env file):
 pdm add python-dotenv

Set Up Azure API Credentials
1. Go to [Azure Portal](https://portal.azure.com/)
2. Create a "Computer Vision Resource" (if you haven’t already).
3. Navigate to "Keys and Endpoint" and copy your API key.
4. Set Up Environment Variables- Create a `.env` file in the project root and add the following credentials:
    ```
    AZURE_CV_KEY=your_azure_computer_vision_key
    AZURE_CV_ENDPOINT=https://your-region.api.cognitive.microsoft.com/
    ```

To initialize the app, run the `flask init-app` command:

```
$ pdm run flask init-app
```

If you just want to try it out, generate fake data with `flask lorem` command then run the app:

```
$ pdm run flask lorem
```

It will create a test account:

* email: `admin@helloflask.com`
* password: `moments`

Now you can run the app:

```
$ pdm run flask run
* Running on http://127.0.0.1:5000/
```

Using the Features

1. Upload Images for Alt Text Generation:
Navigate to /upload. 
Upload an image, and the system will automatically generate alt text.

2. Search Images by Detected Objects: 
Go to /search?q=your_keyword. 
The system will retrieve images with matching detected objects.

## Future Improvements
1. Implement user feedback loops to refine ML-generated descriptions.
2. Optimize database queries for large-scale image search.
3. Explore self-hosted models to reduce dependency on cloud APIs.

## License

This project is licensed under the MIT License (see the
[LICENSE](LICENSE) file for details).
