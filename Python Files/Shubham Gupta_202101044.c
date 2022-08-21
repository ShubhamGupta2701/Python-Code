#include<GL/glut.h>
#include<stdlib.h>
#include<stdio.h>
#include<math.h>

void Init(void)
{
    glClearColor(1.0,1.0,1.0,1.0);
    glColor3f(1.0,0.0,0.0);
    //glPointSize(3.0);
    //    glMatrixMode(GL_PROJECTION);
    //    glLoadIdentity();
    gluOrtho2D(0.0,640.0,0.0,480.0);
}

void setPixel(double xcoordinate, double ycoordinate)
{
    glBegin(GL_POINTS);
    glVertex2d(xcoordinate,ycoordinate);
    glEnd();
    glFlush();
}

void lineDDA(double x0,double y0,double xEnd,double yEnd)
{
    double dx = abs(xEnd-x0);
    double dy = abs(yEnd-y0);
    int steps,k;
    double xIncrement,yIncrement,x=x0,y=y0;

    if(dx>dy)
        steps = dx;
    else
        steps = dy;

    xIncrement = dx/(float)steps;
    yIncrement = dy/(float)steps;
    setPixel(round(x),round(y));

    for(k=1; k<steps; k++)
    {
        x+= xIncrement;
        y+= yIncrement;
        setPixel(round(x),round(y));
    }
}

void Display(void)
{
    glClear(GL_COLOR_BUFFER_BIT);
    lineDDA(300,300,400,300);
    lineDDA(300,320,400,320);
    lineDDA(300,300,300,320);
    lineDDA(400,300,400,320);
    lineDDA(300,200,400,200);
    lineDDA(300,220,400,220);
    lineDDA(300,200,300,220);
    lineDDA(400,200,400,220);
    lineDDA(300,220,380,300);
    lineDDA(320,220,400,300);
    //lineDDA(340,200,360,200);
}

int main(int argc,char *argv[])
{
    glutInit(&argc,argv);
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB);
    glutInitWindowSize(600,600);
    glutInitWindowPosition(50,50);
    glutCreateWindow("DDA Line Algorithum");
    glutDisplayFunc(Display);
    Init();
    glutMainLoop();
    return 0;
}
