class Component {
  $target;
  $props;

  constructor({ $app, $target, $props }) {
    this.$target = $target;
    this.$props = $props;
    this.setEvent();
    $app.appendChild(this.$target);
    this.render();
  }

  mounted() {}
  setEvent() {}
  setState(nextState) {}
  templateBuilder() {
    return ``;
  }
  render() {
    this.$target.innerHTML = this.templateBuilder();
  }
}

class App {
  $target;
  state;
  constructor({ $target }) {
    this.$target = $target;
    this.setUp();
    this.render();
  }

  setUp() {}
  setState() {}
  mounted() {}
  render() {}

  logic1() {}
  logic2() {}
}
