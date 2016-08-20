#!/usr/bin/env dub
/+ dub.sdl:
name "rejection"
dependency "matplotd" version="0.0.1"
+/

S sample(RNG, Pdf, Hat, S)(ref RNG gen, Pdf pdf, Hat hat, S left, S right)
{
    import std.random : uniform;
    for (;;)
    {
        // generate x with density proportional to hat(x)
        S x = uniform!("[]", S)(left, right, gen);
        S y = uniform!("[]", S)(0, 1, gen);
        // check whether the sampled point is within the density
        if (y * hat(x) <= pdf(x))
            return x;
    }
}

void main()
{
    import std.math : PI, sin;
    import std.random: Mt19937;
    alias S = double;
    auto gen = Mt19937(42);

    S[] samples = new S[10_000];
    auto pdf = (S x) => sin(x);
    auto hat = (S x) => 1;
    foreach(i; 0..samples.length)
        samples[i] = sample(gen, pdf, hat, 0, PI);


    string plotDir = "plots";
    import std.file : exists, mkdir;
    import std.path : buildPath;
    if (!plotDir.exists)
        plotDir.mkdir;

    import matplotd.hist;
    HistogramConfig hc = {histType: "step", color:"red"};
    histogram(pdf, samples, plotDir.buildPath("rejection.pdf"), hc);
    hc.cumulative = true;
    histogram(pdf, samples, plotDir.buildPath("rejection_cum.pdf"), hc);
}
