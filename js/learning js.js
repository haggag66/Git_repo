//**  main function **//

// varLetConst();
// variable();
// consoleLog();
// datatype();
// consoleMethodsAndWebAPI();
// ES6();
// varLetConst();
// string();
// concatenation();
// challenge1();
// number();
array();

////////////////////////////////////////////////////////////////
function introdution() {
  console.log("hello world");
}
function variable(){
  let new_variable=60;
  var old_variable=70;
  new_variable=50;
  old_variable=90;
  const constant=40;
}
function consoleLog() {
  let new_variable=60;
  console.log("hello world!");
  console.log(new_variable);
  let message="my name is mohamed haggag";
  console.log(message);
  
}
function datatype(){
  let symbol=Symbol('hello world!');
  let symbol2=Symbol('hello world!');
  console.log(symbol);
  console.log(symbol2);
  console.error(`hello world!`);
  console.log(typeof("hello world!"));
  console.log(typeof(500));
  console.log(typeof(3.3));
  console.log(typeof([1,2,3]));//Array
  console.log(typeof{name:'Mohamed haggag',age:20});//object
  console.log(typeof(2000000000000000000000000n));
  console.log(typeof(undefined));
  console.log(typeof(null));
  console.log(typeof(true));
  console.log(typeof(false));
}
function consoleMethodsAndWebAPI(){
  console.log('log');
  console.error(`error here`);
  console.table(["ali",`omer`,`mohamed`,`haggag`]);
  console.log("My name is %cMohamed Haggag","color:lightblue;font-size:30px;");
  // console is follow Web API
}
function ES6(){
  var myName='haggag';
  console.log("hello "+myName);
  console.log(`hello ${myName}`);
}
function varLetConst() {
  var a=1;
  var a=2;
  console.log(a);

  let b=9;
  // let b=10;    error here
  b=11;    
  console.log(b);

  const c=10;//you can't update this variable
  console.log(c);

  console.log(d);//error but is not disapponte  (rarrange your code) and same error with let and const
  var d=10;

  var e=20;//you can called by window.e but it is mistake in big scale projects
  window.e;
}
function string(){
  console.log("hello 'world'");//no error
  // console.log('hello 'world'');  //error you should use double quotes
  console.log(`hello`);
  console.log("hell\
  o \
  \"world\" \\ ");//to print double quotes
  console.log("hello \n web \n zero");

  let string ="Mohamed Adel Abdo Haggag";
  console.log(string.length);
  console.log(string.charAt(1));//to choose character of string
  console.log(string.indexOf("a",4,10));//to search about character from pos to les
  console.log(string.lastIndexOf("a",4,10));//to search about character from les to pos
  console.log((100).toString());//to convert number to string 
  console.log(parseInt("100"));//convert string to number until if it is at end string but it not work if number is between string 
  let name="   mohamed    haggag   ";
  console.log(name.trim());//to remove many space if space in introdution of string or in end of string  only
  let testUpperCase = "testUpperCase",testLowerCase = "TESTLOWERCASE";
  console.log(testUpperCase.toUpperCase());
  console.log(testLowerCase.toLowerCase());
  console.log(name.trim().toUpperCase().charAt((testUpperCase.length)-1));
  console.log(name.slice(0,-3));//to print string from pos to les without last (les) characater
  console.log(name.slice(3,7));//to print string from pos to les (as longer as substring) 
  
}
function concatenation(){
  let a="my name:";
  let b="Mohamed Haggag";
  console.log(a+" "+b);
  console.log(a,b);
  console.log(`${a} ${b}`);
  console.log(a+"\n"+b);
  console.log(`${a} "" \\ '' 
  ${b} ${3+4}`);
  let des=`<p>hello ${b}</p>`;
  document.write(des);
}
function challenge1(){
  let theTitle="Elzero",theDescription="Elzero web school",theDate="20/10";
  let res=`
  <div>
    <h3>${theTitle}</h3>
    <p>${theDescription}</p>
    <span>${theDate}</span>
  </div>
  `;
  for (let i = 0; i < 4; i++) {
    document.write(res);
    
  }
}
function number(){
  console.log(+100);
  console.log(+"100");
  console.log(-100);
  console.log(-"100");
  console.log(+"-100");
  console.log(-"-100");
  console.log(+"Osama");
  console.log(-"Osama");
  console.log(+"25.5");
  console.log(-2.8);
  console.log(+0xff);
  console.log(+true);
  console.log(+false);
  console.log(+null);
  console.log(-null);
  console.log(-true);
  console.log(-false);
  console.log(Number("100"));




}

function array(){
  let arr = [3,4,5,"mohamed",4.2,'c',[4,5,"haggag"]];
  console.log(arr);
  console.log(`hello ${arr[3]}`);
  console.log(`hello ${arr[3][4]}`);
  console.log(`hello ${arr[6][2][0]}`);
  // a[2]=`adel`; //error here you can't change datatype varible 
  arr[3]=`adel`;
  console.log(arr);
  console.log(typeof(arr));
  console.log(Array.isArray(arr));
  console.log(arr.length);
  // console.log(Array.toString(arr));
  arr[arr.length]="mohamed";
  console.log(arr);
  arr.length=4;
  console.log(arr);
  
}


