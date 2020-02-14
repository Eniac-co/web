<template>
  <div class="home" id="form">
    <el-row>
      <el-col :span="8">
        <el-row>
          <h2 style="color: white" class="follower">n</h2>
          <hr align="center" />
          <!-- <el-divider></el-divider> -->
        </el-row>
        <h2 class="location" align="left">Location: Taipei, Taiwan</h2>
        <h2 class="location" align="left">Type: Remote / Full time</h2>
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
          <h2 class="follower" align="left">saved job: 20</h2>
          <hr />
        </el-row>
        <h2 class="location" align="left">Position: senior full stack engineer</h2>
        <el-row style="margin-top: 15px;">
          <font-awesome-icon
            :icon="['fas', 'envelope-square']"
            size="3x"
            pull="left"
            transform="right-30"
          />
          <font-awesome-icon
            :icon="['fab', 'github-square']"
            size="3x"
            pull="left"
            transform="right-30"
          />
          <font-awesome-icon
            :icon="['fab', 'linkedin']"
            size="3x"
            pull="left"
            transform="right-30"
          />
          <font-awesome-icon
            :icon="['fab', 'stack-overflow']"
            size="3x"
            pull="left"
            transform="right-30"
          />
        </el-row>
        <el-row></el-row>
      </el-col>
    </el-row>
    <br />
    <br />
    <br />
    <el-row :gutter="50">
      <el-col span="16" :offset="4">
        <el-tabs tab-position="left">
          <el-tab-pane label="Working experience">
            <el-row :gutter="20">
              <el-col :span="2" offset="1">
                <h3>Industry:</h3>
              </el-col>
              <el-col :span="20" align="left" offset="1">
                <el-tag
                  :key="tag"
                  v-for="tag in dynamicTags"
                  closable
                  :disable-transitions="false"
                  @close="handleClose(tag)"
                >{{tag}}</el-tag>
                <el-input
                  class="input-new-tag"
                  v-if="inputVisible"
                  v-model="inputValue"
                  ref="saveTagInput"
                  size="small"
                  @keyup.enter.native="handleInputConfirm"
                  @blur="handleInputConfirm"
                ></el-input>
                <el-button v-else class="button-new-tag" size="small" @click="showInput">+ New Tag</el-button>
              </el-col>
            </el-row>
            <el-row style="margin-top: 10px">
              <el-col span="6" :offset="3">
                <el-row style="margin-top: 10px">
                  <el-card class="box-card">
                    <div slot="header" class="clearfix">
                      <span style="font-size: 18px;">Full stack engineer @ xx Company</span>
                      <h5 class="field">FINTECH</h5>
                      <!-- <el-button style="float: right; padding: 3px 0" type="text">操作按钮</el-button> -->
                    </div>
                    <div v-for="o in detail" :key="o" class="text item">{{ o }}</div>
                  </el-card>
                </el-row>
              </el-col>
            </el-row>
          </el-tab-pane>
          <el-tab-pane label="Skill / Project">
            <el-row :gutter="20">
              <el-col :span="2" offset="1">
                <h3>Skill:</h3>
              </el-col>
              <el-col :span="20" align="left">
                <el-tag
                  :key="tag"
                  v-for="tag in dynamicTags"
                  closable
                  :disable-transitions="false"
                  @close="handleClose(tag)"
                >{{tag}}</el-tag>
                <el-input
                  class="input-new-tag"
                  v-if="inputVisible"
                  v-model="inputValue"
                  ref="saveTagInput"
                  size="small"
                  @keyup.enter.native="handleInputConfirm"
                  @blur="handleInputConfirm"
                ></el-input>
                <el-button v-else class="button-new-tag" size="small" @click="showInput">+ New Tag</el-button>
              </el-col>
            </el-row>
            <el-row style="margin-top: 10px">
              <el-col span="6" :offset="3">
                <el-row style="margin-top: 10px">
                  <el-card class="box-card">
                    <div slot="header" class="clearfix">
                      <span style="font-size: 18px;">Pinball web version</span>
                      <h5 class="field">GAME</h5>
                      <!-- <el-button style="float: right; padding: 3px 0" type="text">操作按钮</el-button> -->
                    </div>
                    <div v-for="o in projectDetail" :key="o" class="text item">{{ o }}</div>
                  </el-card>
                </el-row>
              </el-col>
            </el-row>
          </el-tab-pane>
          <el-tab-pane label="others">OTHERS</el-tab-pane>
        </el-tabs>
      </el-col>
    </el-row>
    <el-row :gutter="20">
      <el-col :span="12" :offset="6"></el-col>
    </el-row>
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

.text {
  font-size: 14px;
  text-align: left;
}

.field {
  float: right;
  color: #8b6ae7;
  font-size: 14px;
  padding: 3px 0;
  text-align: left;
}

.item {
  margin-bottom: 18px;
}

.clearfix:before,
.clearfix:after {
  display: table;
  content: "";
}
.clearfix:after {
  clear: both;
}

.box-card {
  width: 500px;
  align-items: center;
}

.el-tag + .el-tag {
  margin-left: 10px;
}
.button-new-tag {
  margin-left: 10px;
  height: 32px;
  line-height: 30px;
  padding-top: 0;
  padding-bottom: 0;
}
.input-new-tag {
  width: 90px;
  margin-left: 10px;
  vertical-align: bottom;
}
</style>

<script>
export default {
  name: "coder",
  data: () => ({
    activeName: "story",
    dynamicTags: ["标签一", "标签二", "标签三"],
    inputVisible: false,
    inputValue: "",
    detail: [
      "1. deploy and impove robustness of company's web",
      "2. lead team of 10"
    ],
    projectDetail: [
      "1. Frontend using Vue",
      "2. Tsinghua Summer project",
      "..."
    ]
  }),

  mounted: function() {
    // this.showCoders();
  },
  methods: {
    handleClose(tag) {
      this.dynamicTags.splice(this.dynamicTags.indexOf(tag), 1);
    },

    showInput() {
      this.inputVisible = true;
      this.$nextTick(_ => {
        this.$refs.saveTagInput.$refs.input.focus();
      });
    },

    handleInputConfirm() {
      let inputValue = this.inputValue;
      if (inputValue) {
        this.dynamicTags.push(inputValue);
      }
      this.inputVisible = false;
      this.inputValue = "";
    }
  }
};
</script>


