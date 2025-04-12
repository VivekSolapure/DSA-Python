class Patterns {
    static rightAngledTriangle(n) {
        for (let i = 0; i < n; i++) {
            console.log('* '.repeat(i + 1));
        }
    }

    static rightAngledNumberPyramid(n) {
        for (let i = 0; i < n; i++) {
            let row = '';
            for (let j = 0; j <= i; j++) {
                row += (j + 1) + ' ';
            }
            console.log(row);
        }
    }

    static rightAngledNumberPyramid2(n) {
        for (let i = 0; i < n; i++) {
            console.log((i + 1 + ' ').repeat(i + 1));
        }
    }

    static invertedRightPyramid(n) {
        for (let i = n; i > 0; i--) {
            console.log('* '.repeat(i));
        }
    }

    static invertedNumberedRightPyramid(n) {
        for (let i = n; i > 0; i--) {
            let row = '';
            for (let j = 0; j < i; j++) {
                row += (j + 1) + ' ';
            }
            console.log(row);
        }
    }

    static starPyramid(n) {
        for (let i = 0; i < n; i++) {
            console.log(' '.repeat(n - i - 1) + '*'.repeat(2 * i + 1));
        }
    }

    static invertedStarPyramid(n) {
        for (let i = n; i > 0; i--) {
            console.log(' '.repeat(n - i) + '*'.repeat(2 * i - 1));
        }
    }

    static diamondStarPattern(n) {
        this.starPyramid(n);
        this.invertedStarPyramid(n - 1);
    }

    static halfDiamondStarPattern(n) {
        this.rightAngledTriangle(n);
        this.invertedRightPyramid(n - 1);
    }

    static binaryNumberTriangle(n) {
        for (let i = 0; i < n; i++) {
            let row = '';
            let start = i % 2 === 0 ? 1 : 0;
            for (let j = 0; j <= i; j++) {
                row += start + ' ';
                start = 1 - start;
            }
            console.log(row);
        }
    }

    static numberCrownPattern(n) {
        for (let i = 0; i < n; i++) {
            let row = '';
            for (let j = 1; j <= i + 1; j++) row += j;
            row += ' '.repeat((n - i - 1) * 2);
            for (let j = i + 1; j > 0; j--) row += j;
            console.log(row);
        }
    }

    static increasingNumberTriangle(n) {
        let num = 1;
        for (let i = 0; i < n; i++) {
            let row = '';
            for (let j = 0; j <= i; j++) {
                row += num++ + ' ';
            }
            console.log(row);
        }
    }

    static increasingLetterTriangle(n) {
        for (let i = 0; i < n; i++) {
            let row = '';
            for (let j = 0; j <= i; j++) {
                row += String.fromCharCode(65 + j) + ' ';
            }
            console.log(row);
        }
    }

    static reverseLetterTriangle(n) {
        for (let i = n; i > 0; i--) {
            let row = '';
            for (let j = 0; j < i; j++) {
                row += String.fromCharCode(65 + j) + ' ';
            }
            console.log(row);
        }
    }

    static alphaRampPattern(n) {
        for (let i = 0; i < n; i++) {
            console.log((String.fromCharCode(65 + i) + ' ').repeat(i + 1));
        }
    }

    static alphaHillPattern(n) {
        for (let i = 0; i < n; i++) {
            let row = ' '.repeat(n - i - 1);
            let char = 65;
            for (let j = 0; j < 2 * i + 1; j++) {
                row += String.fromCharCode(char) + ' ';
                j < i ? char++ : char--;
            }
            console.log(row.trim());
        }
    }

    static alphaTrianglePattern(n) {
        for (let i = 0; i < n; i++) {
            let row = '';
            let char = 65 + n - 1;
            for (let j = 0; j <= i; j++) {
                row += String.fromCharCode(char--) + ' ';
            }
            console.log(row);
        }
    }

    static symmetricVoidPattern(n) {
        for (let i = 0; i < n; i++) {
            let row = '*'.repeat(n - i) + ' '.repeat(2 * i) + '*'.repeat(n - i);
            console.log(row);
        }
        for (let i = n - 1; i >= 0; i--) {
            let row = '*'.repeat(n - i) + ' '.repeat(2 * i) + '*'.repeat(n - i);
            console.log(row);
        }
    }

    static symmetricButterflyPattern(n) {
        for (let i = 0; i < n; i++) {
            let row = '*'.repeat(i + 1) + ' '.repeat((n - i - 1) * 2) + '*'.repeat(i + 1);
            console.log(row);
        }
        for (let i = n - 1; i >= 0; i--) {
            let row = '*'.repeat(i + 1) + ' '.repeat((n - i - 1) * 2) + '*'.repeat(i + 1);
            console.log(row);
        }
    }

    static hollowRectanglePattern(n) {
        for (let i = 0; i < n; i++) {
            let row = '';
            for (let j = 0; j < n; j++) {
                
                row += (i === 0 || i === n - 1 || j===0 || j === n-1 ) ? '*' : ' ';
            }
            console.log(row);
        }
    }

    static rohanTold(n){
        let repeat=0
        let res
        let spaces=n
        for (let i=1;i<=n;i++){
            let space=" ".repeat(spaces-1)
            for(let j=1;j<=i;j++){
                let temp= 
                res=space+j+("*"+j).repeat(repeat)
            }
            console.log(res);
            repeat+=1
            spaces-=1
            
        }
    }
}

// Example calls
// Patterns.rightAngledTriangle(4);
// Patterns.rightAngledNumberPyramid(4);
// Patterns.rightAngledNumberPyramid2(4);
// Patterns.invertedRightPyramid(4);
// Patterns.invertedNumberedRightPyramid(4);
// Patterns.starPyramid(4);
// Patterns.invertedStarPyramid(4);
// Patterns.diamondStarPattern(4);
// Patterns.halfDiamondStarPattern(4);
// Patterns.binaryNumberTriangle(4);
// Patterns.numberCrownPattern(4);
// Patterns.increasingNumberTriangle(5);
// Patterns.increasingLetterTriangle(4);
// Patterns.reverseLetterTriangle(4);
// Patterns.alphaRampPattern(5);
// Patterns.alphaHillPattern(5);
// Patterns.alphaTrianglePattern(3);
// Patterns.symmetricVoidPattern(5);
// Patterns.symmetricButterflyPattern(6);
Patterns.hollowRectanglePattern(6);
// Patterns.rohanTold(3)