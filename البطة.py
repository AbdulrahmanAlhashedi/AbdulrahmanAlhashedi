import pygame
import sys

# تهيئة Pygame
pygame.init()

# إعداد حجم نافذة اللعبة
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("لعبة البطة")

# إعداد ألوان
white = (255, 255, 255)

# تحميل صورة البطة
duck_image = pygame.image.load("duck.png")  # تأكد من أن لديك صورة باسم "duck.png" في نفس مسار الكود
duck_rect = duck_image.get_rect()

# ضبط موقع البطة في البداية
duck_rect.x = screen_width // 2
duck_rect.y = screen_height // 2

# سرعة البطة
speed = 5

# حلقة اللعبة الرئيسية
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # التحكم في البطة باستخدام مفاتيح الأسهم
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        duck_rect.x -= speed
    if keys[pygame.K_RIGHT]:
        duck_rect.x += speed
    if keys[pygame.K_UP]:
        duck_rect.y -= speed
    if keys[pygame.K_DOWN]:
        duck_rect.y += speed
    
    # ملء الشاشة باللون الأبيض
    screen.fill(white)
    
    # رسم البطة على الشاشة
    screen.blit(duck_image, duck_rect)
    
    # تحديث الشاشة
    pygame.display.flip()

    # تحديد معدل تحديث اللعبة
    pygame.time.Clock().tick(60)

# إنهاء Pygame
pygame.quit()
sys.exit()
```

### 3. شرح الكود:

- **تهيئة Pygame**: الكود يبدأ بتهيئة مكتبة Pygame باستخدام `pygame.init()`.