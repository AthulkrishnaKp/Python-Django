
// in python constructor name = __init__ , in javascript constructor name = constructor

class Posts{
    constructor(title,description,author){
        this.title=title
        this.description=description
        this.author=author
    }
    printPost(){
        console.log(this.title,this.description,this.author);
    }
}


var obj=new Posts('post','new post','athul')
console.log(obj.printPost());

// obj.setPost("new post","this is my first post","Athul")
// obj.printPost()

