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
          label="请输入充值金额"
          style="width:200px;"
        ></el-input-number>
      </p>
      <p>
        <el-button plain @click="getCardInfo" style="width:200px">充值</el-button>
      </p>
    </div>
  </div>
</template>

<script>
import axios from "axios";
import qs from "qs";
export default {
  name: "recharge",
  data() {
    return {
      cardInfo: {},
      moeny: 0,
      cardNum: ""
    };
  },
  methods: {
    getCardInfo: function() {
      if (this.moeny !== 0) {
        axios({
          url: "/api/recharge",
          method: "post",
          responseType: "json", // 默认的
          data: qs.stringify({
            sno: this.$cookie.get("sno"),
            moeny: this.moeny
          })
        }).then(res => {
          // eslint-disable-next-line
          console.log(res);
          if (res.data.error_code == 0) {
            this.$message.success("充值成功！");
          } else {
            this.$message.error("充值失败！");
          }
          //eslint-disable-next-line
          // console.log(this.$cookie.get('sno'));
        });
      } else {
        this.$message.error("金额不能为零！");
      }
    }
  }
};
</script>

<style>
</style>