<template>
    <div v-if="user1_data && user2_data">
      <div class="container">
        <span class="name">{{ user1_data["username"] }}</span>
        <nav><router-link to="/about"><button class="btn-11">Назад</button></router-link></nav>
      </div>
      <div align="center">
        <table>
          <tr>
            <td>
              <div class="f">
              <div class="small-square">
                Дата рождения: {{ user1_data["date_of_birth"] }}
              </div>
              <div class="small-square">
                Гендер: {{ user1_data["gender"] }}
              </div>
              <div class="titlesquare" align="center"><b>Мой квадрат Пифагора</b></div>
              <table class="square">
                <tr>
                  <td>
                    <div>{{ user1_data["psychodata"][0] }}</div>
                    <div>Характер</div>
                  </td>
                  <td>
                    <div>{{ user1_data["psychodata"][1] }}</div>
                    <div>Здоровье</div>
                  </td>
                  <td>
                    <div>{{ user1_data["psychodata"][2] }}</div>
                    <div>Удача</div>
                  </td>
                </tr>
                <tr>
                  <td>
                    <div>{{ user1_data["psychodata"][3] }}</div>
                    <div>Энергетика</div>
                  </td>
                  <td>
                    <div>{{ user1_data["psychodata"][4] }}</div>
                    <div>Логика</div>
                  </td>
                  <td>
                    <div>{{ user1_data["psychodata"][5] }}</div>
                    <div>Призвание</div>
                  </td>
                </tr>
                <tr>
                  <td>
                    <div>{{ user1_data["psychodata"][6] }}</div>
                    <div>Познание</div>
                  </td>
                  <td>
                    <div>{{ user1_data["psychodata"][7] }}</div>
                    <div>Трудолюбие</div>
                  </td>
                  <td>
                    <div>{{ user1_data["psychodata"][8] }}</div>
                    <div>Память и ум</div>
                  </td>
                </tr>
              </table>
            </div>
            </td> 
            <td>
              <div class="f">
                <div class="small-square">
                Дата рождения: {{ user2_data["date_of_birth"] }}
              </div>
              <div class="small-square">
                Гендер: {{ user2_data["gender"] }}
              </div>
              <div class="titlesquare" align="center"><b>Квадрат Пифагора {{ user2_data["username"] }}</b></div>
              <table class="square">
                <tr>
                  <td>
                    <div>{{ user2_data["psychodata"][0] }}</div>
                    <div>Характер</div>
                  </td>
                  <td>
                    <div>{{ user2_data["psychodata"][1] }}</div>
                    <div>Здоровье</div>
                  </td>
                  <td>
                    <div>{{ user2_data["psychodata"][2] }}</div>
                    <div>Удача</div>
                  </td>
                </tr>
                <tr>
                  <td>
                    <div>{{ user2_data["psychodata"][3] }}</div>
                    <div>Энергетика</div>
                  </td>
                  <td>
                    <div>{{ user2_data["psychodata"][4] }}</div>
                    <div>Логика</div>
                  </td>
                  <td>
                    <div>{{ user2_data["psychodata"][5] }}</div>
                    <div>Призвание</div>
                  </td>
                </tr>
                <tr>
                  <td>
                    <div>{{ user2_data["psychodata"][6] }}</div>
                    <div>Познание</div>
                  </td>
                  <td>
                    <div>{{ user2_data["psychodata"][7] }}</div>
                    <div>Трудолюбие</div>
                  </td>
                  <td>
                    <div>{{ user2_data["psychodata"][8] }}</div>
                    <div>Память и ум</div>
                  </td>
                </tr>
              </table>
            </div>
            </td>         
          </tr>
        </table>
      </div>
  <div class="titleS"><b>Совместимость</b></div>
  <div class="compare" align="center">
  <table>
      <tr>
          <td>Характеры </td><td>{{ user1_data["psychodata"][0] }}-{{ user2_data["psychodata"][0] }}</td>
      </tr>
      <tr>
          <td>Семейность </td><td>{{ user1_data["psychodata"][13] }}-{{ user2_data["psychodata"][13] }}</td>
      </tr>
      <tr>
          <td>Темперамент </td><td>{{ user1_data["psychodata"][16] }}-{{ user2_data["psychodata"][16] }}</td>
      </tr>
  </table>
  </div>
  </div>
</template>


<script>
import { HTTP } from '../api/common';

export default {
  data() {
    return {
      user1_data: null,
      user2_data: null
    };
  },
  methods: {
    async getUserDataJson(username) {
      console.log("getUserDataJson");

      try {
        const response = await HTTP.get(`/user-data/${username}/`);
        console.log(response);

        if ("data" in response) {
          var user_data_json = response["data"];
          var psychodata_json = JSON.parse(user_data_json["psychodata"]);
          user_data_json["psychodata"] = psychodata_json;
          console.log("UserData found:");
          console.log(user_data_json);
          return user_data_json;
        } else {
          console.log("No UserData found. Unexpected!!!");
        }
      } catch (error) {
        console.log("No UserData found");
        console.error(error);
      }
    },

    async getUser1Data() {
      this.user1_data = await this.getUserDataJson(localStorage.getItem("username"));
      console.log("getUser1Data:", this.user1_data);
    },

    async getUser2Data() {
      var username = this.$route.params.username;
      console.log(`${username}`);
      this.user2_data = await this.getUserDataJson(username);
      console.log("getUser2Data:", this.user2_data);
    },

    onExitClick() {
      console.log("onExitClick")
      localStorage.removeItem("username")
      localStorage.removeItem("token")
      localStorage.removeItem("user_id")
    }
  },
  beforeMount(){
    this.getUser1Data()
    this.getUser2Data()
  }
};
</script>


<style>
.small-square {
  font-size: 20px;
  margin: 5px;
}
.f{
  margin-top: 20px;
  margin-bottom: 20px;
  margin-left: 20px;
  margin-right: 20px;
}
.titlesquare{
  font-size: 25px;
  margin-top: 10px;
  margin-bottom: 10px;
  margin-left: 10px;
  margin-right: 10px;
}
.square{
  font-size: 25px;
}
.btn-11 {
  background: #7986cb;
  font-size: 14px;
  color: white;
  border-radius: 20px;
  box-shadow: 0 7px 0px #3f51b5;
  display: inline-block;
  transition: all .2s;
  position: relative;
  padding: 7px 18px;
  position: relative;
  top: 0;
  cursor: pointer;
  margin:0 10px;
}
 .btn-11:active {
  top: 3px;
  box-shadow: 0 2px 0px #3f51b5;
  transition: all .2s;
}
.titleS{
    font-size: 25px;
}
td{
  text-align: center;
}
.compare{
    font-size: 25px;
    margin-top: 20px;
}
.container {
  display: flex;
  justify-content: space-between;
  align-items: center;
}
.name {
  margin-left: 35px;
  margin-top: 35px;
  font-size: 35px;
}
.button{
 position:static;
 font-size: 14px;
 color: #fff;
 background: #00b4ef;
 border-radius: 30px;
 padding: 10px 25px;
 border: none;
 text-transform: capitalize;
 transition: all 0.5s ease 0s;
}
</style>