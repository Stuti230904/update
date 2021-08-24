import datetime
import pygame
from game import score

pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
width, height = screen.get_size()
font = pygame.font.SysFont('cambria', 28)
font2 = pygame.font.SysFont('cambria', 40)
username1 = ""
text2 = font.render("Enter your username: ", True, (255, 255, 255))

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_BACKSPACE:
                username1 = username1[:-1]
            elif event.key == pygame.K_ESCAPE:
                pygame.quit()
                quit()
            elif event.key == pygame.K_RETURN:
                if username1 == "":
                    default = "Anonymous"
                    username1 = default
                date = datetime.date.today()

                import mysql.connector
                mycur = mysql.connector.connect(
                    host="localhost",
                    user="root",
                    password="stuti23", )
                cur = mycur.cursor()

                databases = ("SHOW DATABASES")
                cur.execute(databases)
                L = []
                for (databases) in cur:
                    L.append(databases[0])
                if "game_data_7" not in L:
                    cur.execute("CREATE DATABASE game_data_7")

                cur.execute("USE game_data_7")
                tables = ("SHOW TABLES")
                cur.execute(tables)

                L2 = []
                for (tables) in cur:
                    L2.append(tables[0])

                if "scores" not in L2:
                    cur.execute("CREATE TABLE Scores (UserName VARCHAR(50), Score INTEGER(5), Date date)")
                cur.execute("Select Username from scores")
                data = ()
                for i in cur:
                    data += i
                if username1 in data:
                    cur.execute("Select score from scores where UserName= '%s'" % username1)
                    for lvl in cur:
                        for l in lvl:
                            if score > l:
                                statement = "Update scores set Score=%s , date= %s where UserName= %s"
                                data = score, date, username1
                                cur.execute(statement, data)
                                mycur.commit()
                else:
                    statement = "INSERT INTO Scores VALUES (%s, %s, %s)"
                    data = username1, score, date
                    cur.execute(statement, data)
                    mycur.commit()
                quit()
            else:
                username1 += event.unicode

    screen.fill((0, 0, 0))
    text3 = font.render(username1, True, (150, 0, 0))
    screen.blit(text3, ((width/2)-50, (height/2)+250))
    screen.blit(text2, ((width/2)-139, (height/2)+200))
    font1 = pygame.font.Font('freesansbold.ttf', 150)
    font2 = pygame.font.SysFont('cambria', 40)
    text = font1.render("Game Over", True, (255, 255, 255))
    from game import score
    text1 = font2.render("Your score was "+str(score), True, (255, 255, 255))
    screen.blit(text, ((width/2)-400, (height/2)-200))
    screen.blit(text1, ((width/2)-150, (height/2+50)))
    pygame.display.flip()