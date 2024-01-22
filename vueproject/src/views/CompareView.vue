<template>
    
    <div class="container">
      <span class="name">Имя</span>
      <nav><router-link to="/"><button class="button">Выход</button></router-link></nav>
     </div>

 <div class="title"><b>Совместимость по квадрату Пифагора</b></div>
 <div class="compare" align="center">
 <table>
    <tr>
        <td>Характеры </td><td>1-1</td>
    </tr>
    <tr>
        <td>Семейность </td><td>1-1</td>
    </tr>
    <tr>
        <td>Темперамент </td><td>1-1</td>
    </tr>
 </table>
</div>
</template>
<script>

</script>
<style>
.title{
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