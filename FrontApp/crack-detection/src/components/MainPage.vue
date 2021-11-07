<template>
  <v-container>
    <v-row class="mt-2" align="center" no-gutters justify="center">
      <v-col cols="9">
        <div class="subtitle-1 mb-1">
          <strong class="blue--text">1.</strong> Please choose photo, that
          contains some cracks on auto window
        </div>
        <v-file-input
          label="Image input"
          filled
          accept="image/*"
          dense
          prepend-icon="mdi-camera"
          @change="photoUploaded"
        >
        </v-file-input>
      </v-col>


      <v-col class="mt-n5"  cols="9">
        <div class="subtitle-1 ">
          <strong class="blue--text">2.</strong> Please select the damaged area
          in the photo.
        </div>
      </v-col>
      <v-col cols="12" md="8" justify="center" align="center">
        <clipper-basic ref="clipper"  class="my-clipper" :src="photoUrl" :ratio="1" preview="my-preview">
          <div
            class="placeholder d-flex flex-column justify-space-between align-center"
            slot="placeholder"
          >
            <v-img
              :aspect-ratio="1 / 1"
              width="400"
              src="../assets/no_image.png"
            ></v-img>
          </div>
        </clipper-basic>
      </v-col>

      <v-col cols="12" md="4" align="left" justify="left">
        <div>

        <clipper-preview name="my-preview" class="my-clipper">
          <div class="placeholder d-flex flex-column justify-space-between align-center"  slot="placeholder">preview area</div>
        </clipper-preview>
        </div>
      </v-col>


      <v-col cols="9">
        <div class="subtitle-1 mb-2">
          <strong class="blue--text">3.</strong> Please choose model, that you
          want to use for classification
        </div>

        <v-autocomplete
          solo
          :disabled="smart"
          v-model="selectedModel"
          :items="models"
        ></v-autocomplete>

        <v-checkbox class="mt-n4" v-model="smart">
          <template v-slot:label>
            <strong>Smart decision </strong>
            <v-tooltip right>
              <template v-slot:activator="{ on, attrs }">

                  <v-icon
                   class="ml-1"
                  color="primary"               
                  
                  v-bind="attrs"
                  v-on="on">mdi-help-circle-outline</v-icon>
                
              </template>
              <span style="width: 100px">Smart decision will try to classify image with all models and will give that result, that most of models choose</span>
            </v-tooltip>
          </template>
        </v-checkbox>

      </v-col>

      <v-col class="mt-3 mb-4" cols="12" align="center" justify="center">
        <v-btn
          color="green"
          elevation="9"
          rounded
          outlined
          :loading="loading"
          :disabled="loading"
          x-large
          @click="getCategory()"
        >
          Classify!
        </v-btn>
      </v-col>

      <v-col v-if="predictedCategory" align="center" justify="center" md="12">
        <div class="text-h3 mb-2">
          Result: <strong class="blue--text">{{ predictedCategory }}</strong>
        </div>
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
import axios from 'axios';

export default {
  name: "MainPage",

  data: () => ({
    photoUrl: "",
    width: 1500,
    models: [
      "Inception_v3",
      "EfficientNet",
      "Resnet_v2",
      "Mobilenet",
      "Nasnet",
    ],
    selectedModel: "Inception_v3",
    predictedCategory: "",
    smart: false,
    loading: false,
    resultImgURL: ''

  }),
  methods: {
    photoUploaded(file) {
      console.log(file);
      this.predictedCategory = '';
      if (file) {
        this.photoUrl = URL.createObjectURL(file);
      }
    },

    getResult() {
      const canvas = this.$refs.clipper.clip();//call component's clip method
      this.resultImgURL = canvas.toDataURL("image/jpeg", 1);//canvas->image
    },

    getCategory(){
      let path = `http://localhost:5000/classify`;
      if(this.smart){
        path += 'Smart'
      }
      this.getResult();
      this.predictedCategory = '';

      this.loading = true; 
      let data = {
        model: this.selectedModel,
        image: this.resultImgURL
      }
      axios.post(path, data)
        .then((response) => {
          this.loading = false; 

          this.predictedCategory = response.data;
          console.log(response);
        }).catch((error) => {
           console.log(error);

        });

     
    }

  },
  computed: {},
};
</script>
<style scoped>
.my-clipper {
  width: 100%;
  max-width: 700px;
}
div.v-input__icon button.v-icon {
  font-size: 144px !important;
}
</style>
