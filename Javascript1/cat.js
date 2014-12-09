var cat = {
    tiredness: 20,
    hunger: 20,
    loneliness: 3,
    happiness: 15,
    obedience: -5000,
    
    status: function()  {
        console.log(this);
    },

    feed: function(food){
        if (food === "wet"){
        console.log("Om nom nom");
        this.hunger = this.hunger - 5;
    }else if("dry"){
        console.log("Meow");
        this.happiness = this.happiness -5;
    }else {
        console.log("Meh");
    }
    console.log(this.status());
    },
    sleep: function(hours){
        if (sleep >= 2){
        console.log("Zzzzz");
        this.tiredness = this.tiredness - 10;
    }else if(sleep < 2){
        console.log("Yawn");
        this.tiredness = this.tiredness - 5;
    }
    console.log(this.status());
    },
    pet: function(minutes){
        if (minutes >5) {
        console.log("Prrrr");
        this.loneliness = this.loneliness - 5;
        this.happiness = this.happiness + 10;
        
    }else {
        console.log("Howl");
        this.loneliness = this.loneliness - 1;
        this.happiness = this.happiness + 5;
    }
    console.log(this.status());
    },
    play: function(toy){
        if (toy === "laser"){
        console.log(":-3");
        this.tiredness = this.tiredness + 10;
        this.happiness = this.happiness + 20;
    }else if (toy === "ball"){
        console.log("The cat scratches you.");
        this.obedience = this.obedience - 10;
    }
    console.log(this.status());
    },
    train: function(tools){
        if (tools === "Harness") {
        console.log("Cat scratches your face and gives you the stink eye.");
        this.obedience = this.obedience -1000;
        this.happiness = this.happiness -10;
    }else if(tools === "Catnip") {
        console.log("hiss");
        this.obedience = this.obedience - 1;
        this.hunger = this.hunger + 4;
    }
    console.log(this.status());
    },

};

