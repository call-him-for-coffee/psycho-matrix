<template>

  <div>
    <div class="container">
      <span class="name">{{ auth_username }}</span>
      <nav><router-link to="/"><button class="btn-11" @click="onExitClick">Выход</button></router-link></nav>
    </div>
    <form @submit.prevent="saveUserData" class="form-horizontal">
      <div class="InputData">
        <div class="title2">Введите ваши данные:</div>
        <div>
          <label for="birthday" class="bd">Дата рождения:</label>
          <input type="date" class="form-control" id="birthday" v-model="selectedDateOfBirth">
        </div>
        <div class="bd">
          <label for="gender">Выберите гендер:</label>
          <input
            id="genderSlider"
            type="range"
            min="-1"
            max="1"
            step="0.01"
            v-model="selectedGender"
          />
          <div><nav>
            <button type="submit" class="btn-11">Сохранить</button>
          </nav></div>
        </div>
      </div>
    </form>


    <div v-if="user_data_json" class="Matrix">
      <div align="center">
      <table>
        <tr>
          <td>
            <div class="f">
            <div class="titlesquare" align="center"><b>Квадрат пифагора</b></div>
            <table class="square">
              <tr>
                <td>
                  <div>{{ user_data_json["psychodata"][0] }}</div>
                  <div>Характер</div>
                </td>
                <td>
                  <div>{{ user_data_json["psychodata"][1] }}</div>
                  <div>Здоровье</div>
                </td>
                <td>
                  <div>{{ user_data_json["psychodata"][2] }}</div>
                  <div>Удача</div>
                </td>
              </tr>
              <tr>
                <td>
                  <div>{{ user_data_json["psychodata"][3] }}</div>
                  <div>Энергетика</div>
                </td>
                <td>
                  <div>{{ user_data_json["psychodata"][4] }}</div>
                  <div>Логика</div>
                </td>
                <td>
                  <div>{{ user_data_json["psychodata"][5] }}</div>
                  <div>Призвание</div>
                </td>
              </tr>
              <tr>
                <td>
                  <div>{{ user_data_json["psychodata"][6] }}</div>
                  <div>Познание</div>
                </td>
                <td>
                  <div>{{ user_data_json["psychodata"][7] }}</div>
                  <div>Трудолюбие</div>
                </td>
                <td>
                  <div>{{ user_data_json["psychodata"][8] }}</div>
                  <div>Память и ум</div>
                </td>
              </tr>
            </table>
          </div>
          </td> 
          <td>
            <div class="info">Дата рождения: {{ user_data_json["date_of_birth"] }}</div>
            <div class="info">Гендер: {{ user_data_json["gender"] }}</div>
          </td>         
        </tr>
      </table>
      </div>
      <div align="left" class="titleS">  Расшифровка квадрата Пифагора</div>
      <div align="left" class="mainS">info</div>
    </div>
    <div v-show="other_users_data_json">
      <div align="center" class="titleS">
        Список участников
      </div>
      <ul class="ul-users">
        <li class="li-users" align="left" v-for="(user, key) in other_users_data_json" :key="key">
          <button @click="onCompareUserClick(user.user)" class="btn-11">Сравнить</button>
          {{ user["username"] }}
        </li>
      </ul>
    </div>
    

  </div>
</template>






<script>
import { HTTP, BASE_URL } from "../api/common";

export default {
  data() {
    return {
      auth_username: "",
      selectedDateOfBirth: "1940-10-09",
      selectedGender: 0,
      user_data_json: null,
      other_users_data_json: null,
    }
  },
  methods: {
    getOtherUsersDataJson() {
      console.log("getOtherUsersData")
      HTTP.get("/user-data/")
      .then(response => {
        var users_data_json = response["data"]
        console.log(users_data_json)
        this.other_users_data_json = users_data_json
      })
    },
    saveUserData() {
      console.log("saveUserData")
      console.log(this.selectedDateOfBirth)
      console.log(this.selectedGender)

      var user_id = localStorage.getItem("user_id")
      var username = localStorage.getItem("username")
      var username_link = `${BASE_URL}users/${user_id}/`
      var payload = {
            user: username_link,
            date_of_birth: this.selectedDateOfBirth,
            gender: this.selectedGender,
            favorite_color: "pink",
      }

      HTTP.post("/user-data/", payload)
      .then(response => {
        console.log(response.data);
        this.$router.push("/about");
      })
      .catch(error => {
        var response = JSON.parse(error.request.responseText);
        if (response['user'] == "user data with this user already exists.") {
          HTTP.put(`/user-data/${username}/`, payload)
          .then(response => {
            console.log(response)
            this.user_data_json = response["data"]
            this.user_data_json["psychodata"] = JSON.parse(this.user_data_json["psychodata"])
            console.log(this.user_data_json)
          })
          .catch(error => {
            var response = JSON.parse(error.request.responseText);
            window.alert("Save UserData failed:\n\n" + JSON.stringify(response));
            console.log(response)
          })
        } else {
          window.alert("Save UserData failed:\n\n" + JSON.stringify(response));
          console.log(response)
        }
      })
    },
    onCompareUserClick(user) {
      console.log(`onCompareUserClicked(${user})`)
    },
    onExitClick() {
      console.log("onExitClick")
      localStorage.removeItem("username")
      localStorage.removeItem("token")
      localStorage.removeItem("user_id")
    }
  },
  beforeMount() {
    console.log("beforeMount")
    this.getOtherUsersDataJson()
    this.auth_username = localStorage.getItem("username")
  }
};



</script>









<style>
.ul-users {
  list-style: none;
  padding: 0;
  margin: 0;
}

.li-users {
  margin-bottom: 8px;
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
  margin-top: 10px;
  margin-bottom: 10px;
  margin-left: 10px;
  margin-right: 10px;
}
.mainS{
  font-size: 20px;
}
td{
  text-align: center;
}
.f{
  margin-top: 20px;
  margin-bottom: 20px;
  margin-left: 20px;
  margin-right: 20px;
}
.info{
  font-size: 25px;
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
.bd{
  font-size: 25px;
}
.title2{
  font-size: 30px;
  margin-top: 30px;
  margin-bottom: 30px;
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
.form-control{
 font-size: 20px;
 background: #f0f0f0;
 border: none;
 margin: 0 0 30px 0;
 border-radius: 20px;
 box-shadow: none;
 padding: 0 25px 0 60px;
 height: 40px;
 transition: all 0.3s ease 0s;
}
</style>