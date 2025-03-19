import cv2

# 윤곽선 검출
def DetectEdges(image):

    # BGR 이미지(세 개의 채널)를 GRAY 이미지(단일채널)로 변환한다
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # 불필요한 노이즈를 줄이기 위해 median blur 적용
    gray = cv2.medianBlur(gray, 5)
    
    return cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 9, 9)


# bilateral filter를 적용하여 윤곽선을 보존하며 이미지를 부드럽게 만든다
def BlurImgae(image):
    return cv2.bilateralFilter(img, 9, 300, 300)


# 이미지 불러오기
img = cv2.imread('image.jpg')

edges = DetectEdges(img)
blured = BlurImgae(img)

# 처리된 이미지와 윤곽선을 합친다
output = cv2.bitwise_and(blured, blured, mask=edges)

# Display the cartoon image
cv2.imshow("CartoonRendering", output)
cv2.waitKey(0)
cv2.destroyAllWindows()

