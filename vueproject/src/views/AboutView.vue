<template>

  <div>
    <div class="container">
      <span class="name">Имя</span>
      <nav><router-link to="/"><button class="button">Выход</button></router-link></nav>
  </div>

    <div class="InputData">
      <div class="title2">Введите ваши данные:</div>
      <div>
        <label for="birthday" class="bd">Дата рождения:</label>
        <input type="date" class="form-control" id="birthday" v-model="birthday">
      </div>
      <div class="bd">
        <label for="gender">Выберите гендер:</label>
        <input type="radio" id="male" value="male" v-model="selectedGender">
        <label for="male">Мужской</label>
    
        <input type="radio" id="female" value="female" v-model="selectedGender">
        <label for="female">Женский</label>
      </div>
    </div>

    <div class="Matrix">
      <div align="center">
      <table>
        <tr>
          <td>
            <div class="f">
            <div class="titlesquare" align="center"><b>Квадрат пифагора</b></div>
            <table class="square">
              <tr>
                <td><div>11</div><div>Характер</div></td><td><div>444</div><div>Здоровье</div></td><td><div>7</div><div>Удача</div></td>
              </tr>
              <tr>
                <td><div>2</div><div>Энергетика</div></td><td><div>5</div><div>Логка</div></td><td><div>88</div><div>Призвание</div></td>
              </tr>
              <tr>
                <td><div>333</div><div>Познание</div></td><td><div>66</div><div>Трудолюбие</div></td><td><div>9</div><div>Память и ум</div></td>
              </tr>
            </table>
          </div>
          </td> 
          <td>
            <div class="info">Дата рождения:</div>
            <div class="info">Гендер:</div>
          </td>         
        </tr>
      </table>
      </div>
      <div align="left" class="titleS">  Расшифровка квадрата Пифагора</div>
      <div align="left" class="mainS">info</div>
      <div align="left" class="titleS">  Список участников</div>
      <div align="left" class="mainS">info<nav><router-link to="/compare"><button class="button">Сравнить</button></router-link></nav></div>
    </div>

  </div>
</template>
<script>
export default {
  data() {
    return {
      birthday: '',
      selectedGender: ''
    }
  }
};
</script>

<style>
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