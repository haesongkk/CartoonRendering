import cv2
import os
import glob

inputfoldername = "./input"
outputfoldername = "./output"
inputextensions = ["*.jpg", "*.png", "*.jpeg"]
outputprefix = "cr_"
endmessage = f"작업이 완료되었습니다. output 폴더를 확인하세요."

# 윤곽선 검출
def DetectEdges(_image):
    gray = cv2.cvtColor(_image, cv2.COLOR_BGR2GRAY)
    gray = cv2.medianBlur(gray, 5)
    return cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 9, 9)

# bilateral filter를 적용하여 윤곽선을 보존하며 이미지를 부드럽게 만든다
def BlurImage(_image):
    return cv2.bilateralFilter(_image, 9, 300, 300)

# 윤곽선과 가공된 이미지를 합친다
def ProcessImage(_image):
    edges = DetectEdges(_image)
    blurred = BlurImage(_image)
    return cv2.bitwise_and(blurred, blurred, mask=edges)

# 폴더 내 특정 확장자를 가진 파일 경로들을 반환한다
def LoadPaths(_folderName, _extensions):
    vImgPath = []
    for ext in _extensions:
        vImgPath.extend(glob.glob(os.path.join(_folderName, ext)))
    return vImgPath 

# main 

# 이미지 파일 (경로) 불러오기
vImgPath = LoadPaths(inputfoldername, inputextensions)

for imgPath in vImgPath:

    # 이미지 불러오기
    image = cv2.imread(imgPath)

    # 이미지 가공
    output = ProcessImage(image)

    #이미지 저장
    imgName = os.path.basename(imgPath) 
    outPath = os.path.join(outputfoldername, f"{outputprefix}{imgName}")
    cv2.imwrite(outPath, output)

# 프로그램 종료
print(endmessage)
cv2.waitKey(0)
cv2.destroyAllWindows()