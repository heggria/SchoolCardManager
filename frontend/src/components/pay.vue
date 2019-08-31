<template>
  <div id="user">
    <div style="margin:40px 50px">
      <p>
        <el-input-number
          v-model="moeny"
          @change="handleChange"
          :min="0"
          :max="999"
          :step="0.01"
          label="请输入支付金额"
          style="width:200px;"
        ></el-input-number>
      </p>
      <p>
        <el-input placeholder="请输入密码" v-model="password" show-password style="width:200px;"></el-input>
      </p>
      <p>
        <el-button plain @click="getCardInfo" style="width:200px">支付</el-button>
      </p>
    </div>
  </div>
</template>

<script>
import axios from "axios";
import qs from "qs";
export default {
  name: "pay",
  data() {
    return {
      cardInfo: {},
      moeny: 0,
      password: "",
      cardNum: ""
    };
  },
  methods: {
    getCardInfo: function() {
      if (this.moeny !== 0) {
        if (this.password !== "") {
          axios({
            url: "/api/pay",
            method: "post",
            responseType: "json", // 默认的
            data: qs.stringify({
              sno: this.$cookie.get("sno"),
              passwd: this.password,
              moeny: this.moeny
            })
          }).then(res => {
            // eslint-disable-next-line
            console.log(res);
            if (res.data.error_code == 0) {
              this.$message.success("支付成功！");
            } else {
              this.$message.error("支付失败！");
            }
            //eslint-disable-next-line
            // console.log(this.$cookie.get('sno'));
          });
        } else {
          this.$message.error("密码不能为空！");
        }
      } else {
        this.$message.error("金额不能为零！");
      }
    }
  }
};
</script>

<style>
</style>