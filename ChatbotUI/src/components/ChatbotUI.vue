<script>
export default {
  data() {
    return {
      text: "",
      messages: [],
      counter: 1,
      userId: null
    };
  },
  methods: {
    sendMessage() {
      this.addMessageSend();
      this.sendMessageReceiveAnswer(this);
      this.text = "";
    },
    addMessageSend() {
      let d = new Date();
      let timeStamp = d.getDate() + '/' + (d.getMonth()+1) + '/' + d.getFullYear() + '   ' +  d.getHours() + ':' + d.getMinutes();  
      let message = {
        id: this.counter,
        message: this.text,
        sender: 0,
        name: "Philip",
        time: timeStamp,
      };
      this.messages.push(message);
      this.counter++;
    },
    addMessageReceive(data) {
      let d = new Date();
      let timeStamp = d.getDate() + '/' + (d.getMonth()+1) + '/' + d.getFullYear() + '   ' +  d.getHours() + ':' + d.getMinutes();
      let message = {
        id: this.counter,
        message: data,
        sender: 1,
        name: "Max",
        time: timeStamp,
      };
      this.messages.push(message);
    },
    sendMessageReceiveAnswer() {
      const requestOptions = {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({
              message: this.text,
              userId: this.userId
            }),
      };
      fetch("http://localhost:7799/send-message", requestOptions)
        .then((response) => response.json())
        .then((data) => {
          this.addMessageReceive(data);
        });
     
    },
    register() {
      const requestOptions = {
        method: "GET",
        headers: { "Content-Type": "application/json" },
      };
      fetch("http://localhost:7799/register", requestOptions)
          .then((response) => response.json())
          .then((data) => {
            this.userId = data;
            console.log(this.userId)
          });
    }
  },
  mounted: async function() {
    await this.register();
    console.log("done")
  },
};

</script>

<template>
  <div id="container">
    <aside>
      <header>
        <input type="text" placeholder="search">
      </header>
      <ul>
        <li>
          <img src="https://cdn-icons-png.flaticon.com/512/4233/4233813.png" alt="" width="50" height="60">
          <div>
            <h2>Max</h2>
            <h3>
              <span class="status green"></span>
              online
            </h3>
          </div>
        </li>
      </ul>
    </aside>
    <main>
      <header>
        <img img src="https://cdn-icons-png.flaticon.com/512/4233/4233813.png" alt="" width="50" height="60">
        <div>
          <h2>Chat with Max</h2>
        </div>
        <img src="https://s3-us-west-2.amazonaws.com/s.cdpn.io/1940306/ico_star.png" alt="">
      </header>
      <ul id="chat">
        <li class="you">
          <div class="entete">
            <span class="status green"></span>
            <h3>0000000000000</h3>
          </div>
          <div class="triangle"></div>
          <div class="message">
            Hello my name is Max. How can I help you?
          </div>
        </li>
        <li v-for="message in messages" :key="message.id" :class="{ me: message.sender === 0 , you: message.sender === 1}">
          <div class="entete">
            <h3>{{ message.time }}</h3>
            <h2>{{ message.name }}</h2>
            <span class="status green"></span>
          </div>
          <div class="triangle"></div>
          <div class="message">
            {{ message.message }}
          </div>
        </li>
      </ul>
      <footer>
        <textarea 
          placeholder="Type your message..."
          :value="text"
          @input="event => text = event.target.value"> </textarea>
        <img src="https://s3-us-west-2.amazonaws.com/s.cdpn.io/1940306/ico_picture.png" alt="">
        <img src="https://s3-us-west-2.amazonaws.com/s.cdpn.io/1940306/ico_file.png" alt="">
        <a href="#" @click="sendMessage" >Send</a>
      </footer>
    </main>
  </div>
</template>

<style>
*{
  box-sizing:border-box;
}
body{
  background-color:#abd9e9;
  font-family:Arial;
}
#container{
  width:750px;
  height:800px;
  background:#eff3f7;
  margin:0 auto;
  font-size:0;
  border-radius:5px;
  overflow:hidden;
}
aside{
  width:260px;
  height:800px;
  background-color:#3b3e49;
  display:inline-block;
  font-size:15px;
  vertical-align:top;
}
main{
  width:490px;
  height:800px;
  display:inline-block;
  font-size:15px;
  vertical-align:top;
}

aside header{
  padding:30px 20px;
}
aside input{
  width:100%;
  height:50px;
  line-height:50px;
  padding:0 50px 0 20px;
  background-color:#5e616a;
  border:none;
  border-radius:3px;
  color:#fff;
  background-image:url(https://s3-us-west-2.amazonaws.com/s.cdpn.io/1940306/ico_search.png);
  background-repeat:no-repeat;
  background-position:170px;
  background-size:30px;
}
aside input::placeholder{
  color:#fff;
}
aside ul{
  padding-left:0;
  margin:0;
  list-style-type:none;
  overflow-y:scroll;
  height:690px;
}
aside li{
  padding:10px 0;
}
aside li:hover{
  background-color:#5e616a;
}
h2,h3{
  margin:0;
}
aside li img{
  border-radius:50%;
  margin-left:20px;
  margin-right:8px;
}
aside li div{
  display:inline-block;
  vertical-align:top;
  margin-top:12px;
}
aside li h2{
  font-size:14px;
  color:#fff;
  font-weight:normal;
  margin-bottom:5px;
}
aside li h3{
  font-size:12px;
  color:#7e818a;
  font-weight:normal;
}

.status{
  width:8px;
  height:8px;
  border-radius:50%;
  display:inline-block;
  margin-right:7px;
}
.green{
  background-color:#58b666;
}
.orange{
  background-color:#ff725d;
}
.blue{
  background-color:#6fbced;
  margin-right:0;
  margin-left:7px;
}

main header{
  height:110px;
  padding:30px 20px 30px 40px;
}
main header > *{
  display:inline-block;
  vertical-align:top;
}
main header img:first-child{
  border-radius:50%;
}
main header img:last-child{
  width:24px;
  margin-top:8px;
}
main header div{
  margin-left:10px;
  margin-right:145px;
}
main header h2{
  font-size:16px;
  margin-bottom:5px;
}
main header h3{
  font-size:14px;
  font-weight:normal;
  color:#7e818a;
}

#chat{
  padding-left:0;
  margin:0;
  list-style-type:none;
  overflow-y:scroll;
  height:535px;
  border-top:2px solid #fff;
  border-bottom:2px solid #fff;
}
#chat li{
  padding:10px 30px;
}
#chat h2,#chat h3{
  display:inline-block;
  font-size:13px;
  font-weight:normal;
}
#chat h3{
  color:#bbb;
}
#chat .entete{
  margin-bottom:5px;
}
#chat .message{
  padding:20px;
  color:#fff;
  line-height:25px;
  max-width:90%;
  display:inline-block;
  text-align:left;
  border-radius:5px;
}
#chat .me{
  text-align:right;
}
#chat .you .message{
  background-color:#58b666;
}
#chat .me .message{
  background-color:#6fbced;
}
#chat .triangle{
  width: 0;
  height: 0;
  border-style: solid;
  border-width: 0 10px 10px 10px;
}
#chat .you .triangle{
  border-color: transparent transparent #58b666 transparent;
  margin-left:15px;
}
#chat .me .triangle{
  border-color: transparent transparent #6fbced transparent;
  margin-left:375px;
}

main footer{
  height:155px;
  padding:20px 30px 10px 20px;
}
main footer textarea{
  resize:none;
  border:none;
  display:block;
  width:100%;
  height:80px;
  border-radius:3px;
  padding:20px;
  font-size:13px;
  margin-bottom:13px;
}
main footer textarea::placeholder{
  color:#ddd;
}
main footer img{
  height:30px;
  cursor:pointer;
}
main footer a{
  text-decoration:none;
  text-transform:uppercase;
  font-weight:bold;
  color:#6fbced;
  vertical-align:top;
  margin-left:333px;
  margin-top:5px;
  display:inline-block;
}
</style>