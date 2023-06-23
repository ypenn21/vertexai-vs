
def ocr(image):
  """
  Takes in an image and returns the text in the image using google cloud vision API libraries.

  Args:
    image: The image to be processed.

  Returns:
    The text in the image.
  """

  # Import the necessary libraries.
  from google.cloud import vision

  # Create a Vision client.
  client = vision.ImageAnnotatorClient()

  # Convert the image to a byte string.
  image_bytes = image.read()

  # Detect text in the image.
  response = client.text_detection(image=image_bytes)

  # Extract the text from the response.
  text = response.full_text_annotation.text

  # Return the text.
  return text
#write a function that takes in local image file and returns the text in the image using google cloud vision API libraries
def ocr_from_file(file_path):
  """
  Takes in a local image file and returns the text in the image using google cloud vision API libraries.

  Args:
    file_path: The path to the image file.

  Returns:
    The text in the image.
  """

  # Open the image file.
  with open(file_path, "rb") as image_file:
    image = image_file.read()

  # Return the text from the image.
  return ocr(image)
