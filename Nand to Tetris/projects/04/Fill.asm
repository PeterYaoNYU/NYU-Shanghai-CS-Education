// This file is part of www.nand2tetris.org
// and the book "The Elements of Computing Systems"
// by Nisan and Schocken, MIT Press.
// File name: projects/04/Fill.asm

// Runs an infinite loop that listens to the keyboard input.
// When a key is pressed (any key), the program blackens the screen,
// i.e. writes "black" in every pixel;
// the screen should remain fully black as long as the key is pressed. 
// When no key is pressed, the program clears the screen, i.e. writes
// "white" in every pixel;
// the screen should remain fully clear as long as no key is pressed.

// Put your code here.

(loop)
    @24576
    D=A
    @finalrow
    M=D
    @SCREEN
    D=A
    @address
    M=D
    @KBD
    D=M
    @paintblack
    D;JNE
    @paintwhite
    D;JEQ

(paintblack)
    @address
    D=M
    @finalrow
    D=M-D
    @loop
    D;JEQ
    @address
    A=M
    M=-1

    @address
    M=M+1
    @paintblack
    0;JMP

(paintwhite)
    @address
    D=M
    @finalrow
    D=M-D
    @loop
    D;JEQ
    @address
    A=M
    M=0

    @address
    M=M+1
    @paintwhite
    0;JMP

// @8191
// D=A
// @rownum
// M=D

// (whiteloop)
//     @KBD
//     D=M
//     @blackloop
//     D;JNE
//     @i
//     M=0
//     @paintwhite
//     0;JMP

//     @SCREEN
//     D=A
//     @address
//     M=D

// (paintwhite)
//     @rownum
//     D=M
//     @i
//     D=D-M
//     @whiteloop
//     D;JEQ

//     @address
//     A=M
//     M=0
//     @address
//     M=M+1
//     @i
//     M=M+1

//     @paintwhite
//     0;JMP

// (blackloop)
//     @KBD
//     D=M
//     @whiteloop
//     D;JEQ
//     @i
//     M=0
//     @SCREEN
//     D=A
//     @address
//     M=D
//     @paintblack
//     0;JMP


// (paintblack)


//     @rownum
//     D=M
//     @i
//     D=D-M
//     @blackloop
//     D;JEQ

//     @address
//     A=M
//     M=-1
//     @address
//     M=M+1

//     @i
//     M=M+1

//     @paintblack
//     0;JMP
