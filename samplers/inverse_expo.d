#!/usr/bin/env dub
/+ dub.sdl:
name "inverse_expo"
dependency "matplotd" version="0.0.1"
+/

/**
Using the inverse function rocks
*/
S sample(S, RNG, FInv)(ref RNG gen, FInv finv)
{
    import std.random : uniform;
    S u = uniform!("[)", S)(0, 1);
    return finv(u);
}

void main(string[] args)
{
    import std.random : Mt19937;
    import std.math : exp, log;

    auto gen = Mt19937(42);
    alias S = double;
    auto finv = (S x) => -log(S(1) - x);

    S[] samples = new S[10_000];
    foreach(i; 0..samples.length)
        samples[i] = sample!S(gen, finv);

    string plotDir = "plots";
    import std.file : exists, mkdir;
    import std.path : buildPath;
    if (!plotDir.exists)
        plotDir.mkdir;

    import matplotd.hist;
    auto pdf = (S x) => exp(-x);
    HistogramConfig hc = {histType: "step", color:"red"};
    histogram(pdf, samples, plotDir.buildPath("inverse_expo.pdf"), hc);
    hc.cumulative = true;
    histogram(pdf, samples, plotDir.buildPath("inverse_expo_cum.pdf"), hc);

    import std.stdio : File;
    import std.algorithm : map, joiner;
    // save values to file for further processing
    auto f = File(plotDir.buildPath("hist_values.csv"), "w");
    f.writeln(samples.map!`a.to!string`.joiner(","));
}
