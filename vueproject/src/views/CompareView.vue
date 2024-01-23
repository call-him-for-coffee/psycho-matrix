<template>
    
    <div class="container">
      <span class="name">Имя</span>
      <nav><router-link to="/"><button class="btn-11">Выход</button></router-link></nav>
     </div>
     <div align="center">
      <table>
        <tr>
          <td>
            <div class="f">
            <div class="titlesquare" align="center"><b>Мой квадрат пифагора</b></div>
            <table class="square">
              <tr>
                <td><div>11</div><div>Характер</div></td><td><div>444</div><div>Здоровье</div></td><td><div>7</div><div>Удача</div></td>
              </tr>
              <tr>
                <td><div>2</div><div>Энергенита</div></td><td><div>5</div><div>Логка</div></td><td><div>88</div><div>Призвание</div></td>
              </tr>
              <tr>
                <td><div>333</div><div>Познание</div></td><td><div>66</div><div>Трудолюбие</div></td><td><div>9</div><div>Память и ум</div></td>
              </tr>
            </table>
          </div>
          </td> 
          <td>
            <div class="f">
            <div class="titlesquare" align="center"><b>Чей-то квадрат пифагора</b></div>
            <table class="square">
              <tr>
                <td><div>11</div><div>Характер</div></td><td><div>444</div><div>Здоровье</div></td><td><div>7</div><div>Удача</div></td>
              </tr>
              <tr>
                <td><div>2</div><div>Энергенита</div></td><td><div>5</div><div>Логка</div></td><td><div>88</div><div>Призвание</div></td>
              </tr>
              <tr>
                <td><div>333</div><div>Познание</div></td><td><div>66</div><div>Трудолюбие</div></td><td><div>9</div><div>Память и ум</div></td>
              </tr>
            </table>
          </div>
          </td>         
        </tr>
      </table>
     </div>
 <div class="titleS"><b>Совместимость по квадрату Пифагора</b></div>
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