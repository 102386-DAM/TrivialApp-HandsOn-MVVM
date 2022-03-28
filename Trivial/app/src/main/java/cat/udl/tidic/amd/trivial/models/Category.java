package cat.udl.tidic.amd.trivial.models;

import androidx.annotation.NonNull;

import cat.udl.tidic.amd.trivial.R;

public enum Category {
    net,
    os,
    db,
    patterns;

    @NonNull
    @Override
    public String toString() {
        switch (this){
            case db: return "Databases";
            case os: return "Operating Systems";
            case net: return "Network";
            case patterns: return "Design Patterns";
            default: return "";
        }
    }

    public int getColor() {
        switch (this){
            case db: return R.color.trivial_blue;
            case os: return R.color.trivial_orange;
            case net: return  R.color.trivial_green;
            case patterns: return  R.color.trivial_pig;
            default: return R.color.black;
        }
    }
}