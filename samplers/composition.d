#!/usr/bin/env dub
/+ dub.sdl:
name "composition"
dependency "matplotd" version="0.0.1"
dependency "mir" version="0.16.0-alpha6"
+/

// composition/mixture sampling
S sample(S, RNG, Sampler)(ref RNG gen, Sampler[] samplers, S[] probs)
{
    import mir.random.discrete : discrete;
    // pick a sampler with prob_i
    auto ds = discrete(probs);
    return samplers[ds(gen)](gen);
}

void main()
{
    import std.math : abs, PI, sin;
    import std.random: Mt19937, uniform;
    alias S = double;
    auto gen = Mt19937(42);

    alias Sampler = S delegate(ref typeof(gen) gen);
    S[] probs = [0.3, 0.7];
    Sampler[] samplers = new Sampler[probs.length];
    samplers[0] = (ref typeof (gen) gen) {
        import std.math : log;
        auto finv = (S x) => -log(S(1) - x);
        S u = uniform!("[)", S)(0, 0.8);
        return finv(u);
    };

    samplers[1] = (ref typeof (gen) gen) {
        return uniform!("[]", S)(2, 3, gen);
    };

    S[] samples = new S[1_000_000];
    foreach(i; 0..samples.length)
        samples[i] = sample!S(gen, samplers, probs);

    string plotDir = "plots";
    import std.file : exists, mkdir;
    if (!plotDir.exists)
        plotDir.mkdir;

    import matplotd.hist;
    HistogramConfig hc = {histType: "step", color:"red"};
    histogram(samples, "plots/sin4.pdf", hc);
    hc.cumulative = true;
    histogram(samples, "plots/sin4_cum.pdf", hc);
}
