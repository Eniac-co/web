<template>
  <div class="home" id="form">
    <el-row :gutter="20">
      <el-col :span="8">
        <el-row>
          <h2 class="follower" align="left">your follower: 20</h2>
          <hr />
          <!-- <el-divider></el-divider> -->
        </el-row>
        <h2 class="location" align="left">location: Taipei, Taiwan</h2>
        <el-row></el-row>
        <el-row></el-row>
      </el-col>
      <el-col :span="8">
        <el-row>
          <div>
            <el-avatar shape="square" :size="150" :src="profilePic" @error="errorHandler">
              <img src="https://cube.elemecdn.com/e/fd/0fc7d20532fdaf769a25683617711png.png" />
            </el-avatar>
          </div>
        </el-row>
        <el-row>
          <h1></h1>
        </el-row>
        <el-row align="bottom" type="flex" justify="center">
          <h1>Alison Zhang</h1>
        </el-row>
      </el-col>
      <el-col :span="8">
        <el-row>
          <h2 class="follower" align="left">your follower: 20</h2>
          <hr />
        </el-row>
        <h2 class="location" align="left">location: Taipei, Taiwan</h2>
        <el-row></el-row>
        <el-row></el-row>
      </el-col>
    </el-row>
    <br />
    <br />
    <el-row :gutter="50">
      <el-col>
        <div>
          <el-tabs stretch v-model="activeName" @tab-click="handleClick" type="border-card">
            <el-tab-pane label="story" name="story">style</el-tab-pane>
            <el-tab-pane label="experience" name="experience">
              <el-col :span="12" :offset="6">
                <div class="block">
                  <el-timeline>
                    <el-timeline-item timestamp="2018/4/12" placement="top">
                      <el-card>
                        <h4>更新 Github 模板</h4>
                        <p>王小虎 提交于 2018/4/12 20:46王小jjjj虎 提交于 2018/4/12 20:46</p>
                      </el-card>
                    </el-timeline-item>
                    <el-timeline-item timestamp="2018/4/3" placement="top">
                      <el-card>
                        <h4>更新 Github 模板</h4>
                        <p>王小虎 提交于 2018/4/3 20:46王小虎 提交于 2018/4/12 20:46</p>
                      </el-card>
                    </el-timeline-item>
                    <el-timeline-item timestamp="2018/4/2" placement="top">
                      <el-card>
                        <h4>更新 Github 模板</h4>
                        <p>王小虎 提交于 2018/4/2 20:46王小虎 提交于 2018/4/12 20:46</p>
                      </el-card>
                    </el-timeline-item>
                  </el-timeline>
                </div>
              </el-col>
            </el-tab-pane>
          </el-tabs>
        </div>
      </el-col>
    </el-row>
    <el-row :gutter="20">
      <el-col :span="12" :offset="6"></el-col>
    </el-row>
    <!--                <h1 class=" display-3 font-weight-bold mu-4 mb-4 grey&#45;&#45;text text&#45;&#45;darken-2">Info</h1>-->
    <!-- <p class="subheading">stay connected with us!</p>
                <el-col :span="12" :offset="6" :align="center" >
                    <el-form>
                        <el-form-item label="姓名" prop="name">
                            <el-input v-model="name"></el-input>
                        </el-form-item>
                        <el-form-item label="邮箱" prop="email">
                            <el-input v-model="mail"></el-input>
                        </el-form-item>
                        <el-form-item label="skype" prop="skype" >
                            <el-input v-model="skype" ></el-input>
                        </el-form-item>
                        <el-form-item label="手机号码" prop="phone" >
                            <el-input v-model="phone" ></el-input>
                        </el-form-item>
                        <el-form-item label="何种技术岗位符合您的技术背景">
                          <el-checkbox-group v-model="skillList" >
                            <el-checkbox label="全棧工程師(Node+React)"></el-checkbox>
                            <el-checkbox label="全棧工程師(其他框架)"></el-checkbox>
                            <el-checkbox label="前端工程師(React)"></el-checkbox>
                            <el-checkbox label="前端工程師(其他框架)"></el-checkbox>
                            <el-checkbox label="DevOps工程师"></el-checkbox>
                            <el-checkbox label="移动端开发工程师(Swift or React Native)"></el-checkbox>
                            <el-checkbox label="AI工程师(NLP)"></el-checkbox>
                            <el-checkbox label="AI工程师(CV)"></el-checkbox>
                            <el-checkbox label="AI工程师(其他领域应用)"></el-checkbox>
                            <el-checkbox label="数据科学家(data scientist)"></el-checkbox>
                          </el-checkbox-group>
                        </el-form-item>
                        <el-form-item label="英语程度">
                          <el-radio-group v-model="english">
                            <el-radio label="佳，能听懂英语母语人士的表述且无需对方多次重复。自身英语口说也能让对方轻易了解"></el-radio>
                            <el-radio label="一般。沟通语速慢些的情况下能正常交流"></el-radio>
                            <el-radio label="无法进行口语交流。但能透过英语书信交流（email, slack, etc）"></el-radio>
                          </el-radio-group>
                        </el-form-item>
                        <el-form-item>
                            <el-button @click="storeCoders()">submit</el-button>
                        </el-form-item>
                    </el-form>
    </el-col>-->

    <!--        <el-input v-model="username" placeholder="username" style="display:inline-table; width: 30%; float:left"></el-input>-->
    <!--        <el-input v-model="phone" placeholder="phone" style="display:inline-table; width: 30%; float:left"></el-input>-->
    <!--        <el-input v-model="mail" placeholder="email" style="display:inline-table; width: 30%; float:left"></el-input>-->
    <!--        <el-input v-model="skype" placeholder="skype" style="display:inline-table; width: 30%; float:left"></el-input>-->
    <!--        <el-button type="primary" @click="storeCoders()" style="float:left; margin: 2px;">submit</el-button>-->

    <!--    <el-row>-->
    <!--      <el-table :data="coderList" style="width: 100%" border>-->
    <!--        <el-table-column prop="name" label="username" min-width="100">-->
    <!--          <template scope="scope"> {{ scope.row.name }}</template>-->
    <!--        </el-table-column>-->
    <!--        <el-table-column prop="phone" label="id" min-width="100">-->
    <!--          <template scope="scope"> {{ scope.row.phone }}</template>-->
    <!--        </el-table-column>-->
    <!--      </el-table>-->
    <!--    </el-row>-->
  </div>
</template>

<style>
#form {
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
h1 {
  margin-top: 10px;
}
h2.follower {
  margin-bottom: 15px;
  margin-left: 80px;
}
h2.location {
  margin-top: 15px;
  margin-left: 80px;
}
</style>

<script>
export default {
  name: "home",
  data: () => ({
    profilePic: "../logo.png",
    name: "",
    password: "",
    skype: "",
    phone: "",
    mail: "",
    coderList: [],
    errors: [],
    skillList: [],
    english: [],
    activeName: "story"
  }),

  mounted: function() {
    this.showCoders();
  },
  methods: {
    showCoders() {
      this.$http.get("http://127.0.0.1:8000/api/showCoders").then(response => {
        const res = JSON.parse(response.bodyText);
        console.log(res);
        // eslint-disable-next-line eqeqeq
        if (res.errorNum === 0) {
          this.coderList = res["coder"];
        } else {
          this.$message.error("fail to load coders");
          console.log(res["msg"]);
        }
      });
    },
    storeCoders() {
      this.$http
        .post(
          "http://127.0.0.1:8000/api/registerCoders",
          {
            username: this.name,
            phone: this.phone,
            skype: this.skype,
            mail: this.mail
          },
          { emulateJSON: true }
        )
        .then(response => {
          const res = JSON.parse(response.bodyText);
          console.log(res);
          // eslint-disable-next-line eqeqeq
          if (res.errorNum === 0) {
            // this.coderList = res['coder']
            console.log(res["msg"]);
          } else {
            this.$message.error("fail to load coders");
            console.log(res["msg"]);
          }
        });
    },
    checkForm: function(e) {
      this.errors = [];

      if (!this.name) {
        this.errors.push("Name required.");
      }
      if (!this.mail) {
        this.errors.push("Email required.");
      } else if (!this.validEmail(this.mail)) {
        this.errors.push("Valid email required.");
      }

      if (!this.errors.length) {
        return true;
      }
      e.preventDefault();
    },
    validEmail: function(mail) {
      // eslint-disable-next-line no-useless-escape
      var re = /^(([^<>()\[\]\\.,;:\s@"]+(\.[^<>()\[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/;
      return re.test(mail);
    },
    errorHandler() {
      return True;
    },
    handleClick(tab, event) {
      console.log(tab, event);
      Ｆ;
    }
  }
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
h1,
h2 {
  font-weight: normal;
}

ul {
  list-style-type: none;
  padding: 0;
}

li {
  display: inline-block;
  margin: 0 10px;
}

a {
  color: #42b983;
}
</style>
