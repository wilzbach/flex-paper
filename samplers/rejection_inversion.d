#!/usr/bin/env dub
/+ dub.sdl:
name "rejection_inversion"
dependency "matplotd" version="0.0.1"
+/

S sample(S, RNG, Pdf, Hat, HatInv)(ref RNG gen, Pdf pdf, Hat hat, HatInv hatInvCDF)
{
    import std.random : uniform;
    for (;;)
    {
        S u = uniform!("[]", S)(0, 1, gen);
        // generate x with density proportional to hat(x)
        S x = hatInvCDF(u);

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
    auto hatInvCDF = (S u) => u * PI;
    foreach(i; 0..samples.length)
        samples[i] = sample!S(gen, pdf, hat, hatInvCDF);

    // plot the values
    string plotDir = "plots";
    import std.file : exists, mkdir;
    import std.path : buildPath;
    if (!plotDir.exists)
        plotDir.mkdir;

    import matplotd.hist;
    HistogramConfig hc = {histType: "step", color: "red"};
    histogram(pdf, samples, plotDir.buildPath("rejection_inversion.pdf"), hc);
    hc.cumulative = true;
    histogram(pdf, samples, plotDir.buildPath("rejection_inversion.pdf"), hc);
}
