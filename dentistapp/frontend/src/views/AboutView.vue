<template>
  <TheHeader :logged_in="false"/>
  <div class="about container bright">
    <img alt="Nas tim" style="width: 70%;max-height: 100%" src="../assets/tim.jpg">
    <HelloWorld msg="O nama"/>
    <p style="text-align: justify; text-justify: inter-word;">Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aliquam facilisis commodo enim, eget mollis dui lacinia non. Nam lectus enim, ultrices sed viverra vel, efficitur eget est. Aliquam erat volutpat. Nam lectus purus, suscipit quis congue ut, vehicula eu elit. Etiam eu ex nisl. Maecenas non placerat nulla, quis consequat leo. Praesent tristique lacinia felis ut ultricies. Vivamus rhoncus placerat turpis, ut facilisis ipsum faucibus a. Interdum et malesuada fames ac ante ipsum primis in faucibus. Nam vel auctor neque, non porta elit. Fusce et nisl lacinia, egestas dolor vel, faucibus ex.
    Nulla sed pharetra justo, a viverra sem. Cras at enim id leo vestibulum consequat id non quam. Integer cursus enim et elit dictum, a tincidunt augue tincidunt. Mauris at massa in quam cursus feugiat. Praesent est velit, eleifend ut dolor quis, feugiat posuere mi. In sodales massa dictum, tempor augue ac, volutpat eros. Vivamus dui ligula, euismod id scelerisque quis, suscipit at libero. Nam pharetra lorem sit amet ultrices convallis. Nullam vitae mauris sollicitudin, tempor augue nec, vestibulum quam. Proin convallis iaculis laoreet. Aliquam convallis ultricies purus non pretium. Nullam consequat bibendum purus, sed sollicitudin nunc dignissim sed. Praesent condimentum, augue non convallis tempor, leo elit aliquet turpis, nec semper nisl metus ornare felis.
    Nulla at suscipit massa. Nullam ac urna lobortis, pulvinar urna vel, eleifend metus. Aenean quis lobortis metus, eget tincidunt massa. Curabitur vulputate, leo quis pretium mattis, nisi mauris aliquam quam, et placerat diam neque quis turpis. Nam vel pharetra leo. Aliquam tristique rutrum molestie. Cras nulla ipsum, finibus vel iaculis nec, feugiat a lacus. Maecenas viverra scelerisque felis, eu lacinia neque tincidunt ut.
    Etiam sapien metus, viverra sit amet porttitor vitae, placerat eu sem. Maecenas neque leo, ornare id ullamcorper vitae, ullamcorper vel dolor. Mauris euismod lacus eu erat mollis efficitur. Nullam nec accumsan eros, a sodales leo. Donec vel pulvinar sem, viverra pellentesque turpis. Curabitur tristique quam vitae hendrerit molestie. Nulla facilisi.
    Praesent risus nibh, placerat sed dolor nec, faucibus consequat sem. Integer a turpis et velit blandit sodales ut vel mi. Duis molestie id dolor sed hendrerit. Duis in ante ut lacus dictum pharetra at non lectus. Cras erat eros, gravida condimentum placerat id, porta vitae ex. Donec at aliquet quam. Mauris quis cursus leo, sed dignissim dolor.
    </p>
  
  </div>
</template>

<script>
// @ is an alias to /src
import HelloWorld from '@/components/HelloWorld.vue'
import TheHeader from '@/components/TheHeader.vue'

export default {
  name: 'AboutView',
  components: {
    HelloWorld,
    TheHeader
  }
}
</script>