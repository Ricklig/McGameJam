// BEGIN mystery code o0o0o0o0o -- particles
class hightlightLane{
  constructor(hostX, decayTime) {
    app.stage.addChild(this.highlight);
    this.decayTime = decayTime;

    var shape = new PIXI.Graphics();
    shape.lineStyle(0);
    shape.beginFill(0xFF0000, 0.2);
    shape.drawRect(0, 0, 85, app.screen.height);
    shape.endFill();

    this.highlight = new PIXI.Sprite(app.renderer.generateTexture(shape));
    # beam.anchor.set(0,1);
    // Position
    beam.x = hostX;
    beam.y = 0;

    app.ticker.add((delta) => this.update(delta));
  }
  update(delta){
    let extinct = true;
    this.beams[i].alpha -= 0.4*delta/this.decayTime;
    if (this.beams[i].alpha > 0){
      extinct = false;
    }
  }
}
