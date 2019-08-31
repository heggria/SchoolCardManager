<template>
  <div id="login">
    <div style="width:300px;margin:0 auto;">
      <div style="margin:10px;width:280px;">
        <el-button round style="width:100%;" @click="setReportLoss()" :type="state">{{text}}</el-button>
      </div>
    </div>
  </div>
</template>

<script>
import axios from "axios";
import qs from "qs";
export default {
  name: "reportLoss",
  components: {},
  data() {
    return {
      flag: 0,
      text: "",
      state: 'success'
    };
  },
  created: function() {
    axios({
      url: "/api/getReportLoss",
      method: "post",
      responseType: "json", // 默认的
      data: qs.stringify({
        sno: this.$cookie.get("sno")
      })
    }).then(res => {
      // eslint-disable-next-line
      console.log(res);
      if (res.data.rLCode === 0) {
        this.flag = 0;
        this.text = "本卡未挂失";
      } else {
        this.flag = 1;
        this.text = "本卡已挂失";
      }
    });
  },
  methods: {
    setReportLoss: function() {
      if (this.flag === 0) {
        axios({
          url: "/api/reportLoss",
          method: "post",
          responseType: "json", // 默认的
          data: qs.stringify({
            sno: this.$cookie.get("sno")
          })
        }).then(res => {
          // eslint-disable-next-line
          console.log(res);
          if (res.data.error_code == 0) {
            this.flag = 1;
            this.text = "本卡已挂失";
            this.state='warning';
            this.$message.success = "挂失成功!";
          } else {
            this.flag = 0;
            this.text = "本卡未挂失";
            this.state='success';
            this.$message.success = "挂失失败!";
          }
        });
      } else {
        axios({
          url: "/api/cancelReportLoss",
          method: "post",
          responseType: "json", // 默认的
          data: qs.stringify({
            sno: this.$cookie.get("sno")
          })
        }).then(res => {
          // eslint-disable-next-line
          console.log(res);
          if (res.data.error_code == 0) {
            this.flag = 0;
            this.text = "本卡未挂失";
            this.state='success';
            this.$message.success = "取消挂失成功!";
          } else {
            this.flag = 1;
            this.text = "本卡已挂失";
            this.state='warning';
            this.$message.success = "取消挂失失败!";
          }
        });
      }
    }
  }
};
</script>