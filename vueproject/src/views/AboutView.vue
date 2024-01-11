<template>
  <div>
    <div class="container">
      <span class="name">Имя</span>
      <nav><router-link to="/"><button class="button">Выход</button></router-link></nav>
    </div>
    <div>
      <div class="title2">Ведите ваши данные:</div>
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